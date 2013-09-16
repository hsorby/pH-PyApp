
from PySide import QtCore, QtOpenGL

#import opencmiss
from opencmiss.zinc.context import Context
from opencmiss.zinc.field import Field
from opencmiss.zinc.sceneviewer import SceneViewerInput, SceneViewer
from opencmiss.zinc.spectrum import SpectrumComponent

# Create a button map of Qt mouse buttons to Zinc input buttons
button_map = {QtCore.Qt.LeftButton: SceneViewerInput.INPUT_BUTTON_LEFT, QtCore.Qt.MiddleButton: SceneViewerInput.INPUT_BUTTON_MIDDLE, QtCore.Qt.RightButton: SceneViewerInput.INPUT_BUTTON_RIGHT}

class ZincWidget(QtOpenGL.QGLWidget):
    
    # init start
    def __init__(self, parent = None):
        '''
        Call the super class init functions, create a Zinc context and set the scene viewer handle to None.
        '''
        
        QtOpenGL.QGLWidget.__init__(self, parent)
        print(self.sizeHint())
        # Create a Zinc context from which all other objects can be derived either directly or indirectly.
        #print(opencmiss.zinc.__version__)
        self._context = Context("axisviewer")
        self._scene_viewer = None
        # init end

    def sizeHint(self):
        '''
        Let the layout manager know the preferred size of the widget.
        '''
        return QtCore.QSize(600, 350)
    
    # initializeGL start
    def initializeGL(self):
        '''
        Initialise the Zinc scene for drawing the lungs.  
        '''
        
        # Get the default region to create a point in.
        default_region = self._context.getDefaultRegion()
        
        # Get the graphics module from the context
        graphics_module = self._context.getGraphicsModule()

        # From the graphics module get the scene viewer module.
        scene_viewer_module = graphics_module.getSceneViewerModule()
        
        # From the scene viewer module we can create a scene viewer, we set up the 
        # scene viewer to have the same OpenGL properties as the QGLWidget.
        self._scene_viewer = scene_viewer_module.createSceneViewer(SceneViewer.BUFFERING_MODE_DOUBLE, SceneViewer.STEREO_MODE_ANY)
        
        # Get the glyph module from the graphics module and define the standard glyphs
        glyph_module = graphics_module.getGlyphModule()
        glyph_module.defineStandardGlyphs()
        
        material_module = graphics_module.getMaterialModule()
        material_module.defineStandardMaterials()
        tissue = material_module.findMaterialByName('tissue')
        
        # Once the scenes have been enabled for a region tree you can get a valid 
        # handle for a scene and then populate the scene with graphics.
        scene = graphics_module.getScene(default_region)
        
        # We use the beginChange and endChange to wrap any immediate changes and will
        # streamline the rendering of the scene.
        scene.beginChange()
        
        # Create a filter for visibility flags which will allow us to see our graphic.  By default graphics
        filter_module = graphics_module.getFilterModule()
        # are created with their visibility flags set to on (or true).
        graphics_filter = filter_module.createFilterVisibilityFlags()
        
        spectrum_module = graphics_module.getSpectrumModule()
        
        # Set the graphics filter for the scene viewer otherwise nothing will be visible.
        self._scene_viewer.setFilter(graphics_filter)
        
        default_region.readFile('lungs.exregion')
        field_module = default_region.getFieldModule()
        self._defineDrivingFields(field_module)
        self._createSpectrum(spectrum_module)
        self._data_field = field_module.createConstant(-1)
                
        # Create the surface graphics
        graphic = scene.createGraphicSurfaces()
        graphic.setDomainType(Field.DOMAIN_MESH_HIGHEST_DIMENSION)
        graphic.setCoordinateField(self._inflated_coordinates)
        graphic.setMaterial(tissue)
        graphic.setDataField(self._data_field)
        graphic.setSpectrum(self._spectrum)

        self._scene_viewer.setScene(scene)

        # Let the rendition render the scene.
        scene.endChange()
        self._scene_viewer.viewAll()
        # initializeGL end
        
    def _createSpectrum(self, spectrum_module):
        '''
        Create a spectrum with a single component.
        '''
        self._spectrum = spectrum_module.createSpectrum()
        self._spectrum.setMaterialOverwrite(False)
        self._spectrum_component = self._spectrum.createComponent()
        self._spectrum_component.setColourMapping(SpectrumComponent.COLOUR_MAPPING_RAINBOW)
        self._spectrum_component.setRangeMinimum(0)
        self._spectrum_component.setRangeMaximum(1)

    def _defineDrivingFields(self, field_module):
        '''
        define the driving fields for the lung expansion.
        '''
        coordinates = field_module.findFieldByName('coordinates')
        offset = field_module.createConstant([0, -60, -520])
        oc = coordinates + offset

        self._time_value = field_module.createConstant(0)
        self._z_dir = field_module.createConstant([0, 0.03, 0.08])
        self._y_dir = field_module.createConstant([0.04, 0.08, 0])
        
        pi_2 = field_module.createConstant(3.14159*0.5)
        tpi_2 = self._time_value*pi_2
        sin_tpi_2 = field_module.createSin(tpi_2)
        cos_tpi_2 = field_module.createCos(tpi_2)
        one = field_module.createConstant(1)
        one_minus_cos_tpi_2 = one - cos_tpi_2
        
        tzdir = sin_tpi_2*self._z_dir
        zoc = oc*tzdir
        
        tydir = one_minus_cos_tpi_2*self._y_dir
        yoc = oc*tydir
        
        yzoc = yoc + zoc
        
        self._inflated_coordinates = coordinates + yzoc
        
    def setRange(self, rangeMin, rangeMax):
        '''
        Set the maximum and minimum values for the spectrum.
        '''
        self._spectrum_component.setRangeMinimum(rangeMin)
        self._spectrum_component.setRangeMaximum(rangeMax)
        self.updateGL()
    
    def setSpectrumValue(self, value):
        '''
        Set the value to be used for the spectrum data.
        '''
        default_region = self._context.getDefaultRegion()
        field_module = default_region.getFieldModule()
        field_cache = field_module.createCache()
        self._data_field.assignReal(field_cache, value)
        self.updateGL()
    
    def showSpectrum(self, value):
        '''
        Show the spectrum for the lung surface.  If the value passed
        is outside the range of the spectrum then the material for 
        the lung surface will be visible.
        '''
        default_region = self._context.getDefaultRegion()
        field_module = default_region.getFieldModule()
        field_cache = field_module.createCache()
        self._data_field.assignReal(field_cache, value)
        self.updateGL()
        
    def setDownwardExpansion(self, expansion):
        '''
        Set the downward expansion values for the lung expansion.  The input should be
        a list of length 3.  The default values are [0.0, 0.03, 0.08]
        '''
        default_region = self._context.getDefaultRegion()
        field_module = default_region.getFieldModule()
        field_cache = field_module.createCache()
        self._z_dir.assignReal(field_cache, expansion)
        
    def setLateralExpansion(self, expansion):
        '''
        Set the lateral expansion values for the lung expansion.  The input should be
        a list of length 3.  The default values are [0.04, 0.08, 0.0]
        '''
        default_region = self._context.getDefaultRegion()
        field_module = default_region.getFieldModule()
        field_cache = field_module.createCache()
        self._y_dir.assignReal(field_cache, expansion)
        
    def setTime(self, value):
        '''
        Set the time value for the lung.  The value should be between [0, 1].
        '''
        default_region = self._context.getDefaultRegion()
        field_module = default_region.getFieldModule()
        field_cache = field_module.createCache()
        self._time_value.assignReal(field_cache, value)
        self.updateGL()
    
    # paintGL start
    def paintGL(self):
        '''
        Render the scene for this scene viewer.  The QGLWidget has already set up the
        correct OpenGL buffer for us so all we need do is render into it.  The scene viewer
        will clear the background so any OpenGL drawing of your own needs to go after this
        API call.
        '''
        self._scene_viewer.renderScene()
        # paintGL end

    # resizeGL start
    def resizeGL(self, width, height):
        '''
        Respond to widget resize events.
        '''
        self._scene_viewer.setViewportSize(width, height)
        # resizeGL end

    def mousePressEvent(self, mouseevent):
        '''
        Inform the scene viewer of a mouse press event.
        '''
        scene_input = self._scene_viewer.getInput()
        scene_input.setPosition(mouseevent.x(), mouseevent.y())
        scene_input.setType(SceneViewerInput.INPUT_EVENT_TYPE_BUTTON_PRESS)
        scene_input.setButton(button_map[mouseevent.button()])
            
        self._scene_viewer.processInput(scene_input)
        
    def mouseReleaseEvent(self, mouseevent):
        '''
        Inform the scene viewer of a mouse release event.
        '''
        scene_input = self._scene_viewer.getInput()
        scene_input.setPosition(mouseevent.x(), mouseevent.y())
        scene_input.setType(SceneViewerInput.INPUT_EVENT_TYPE_BUTTON_RELEASE)
        scene_input.setButton(button_map[mouseevent.button()])
            
        self._scene_viewer.processInput(scene_input)
        
    def mouseMoveEvent(self, mouseevent):
        '''
        Inform the scene viewer of a mouse move event and update the OpenGL scene to reflect this
        change to the viewport.
        '''
        scene_input = self._scene_viewer.getInput()
        scene_input.setPosition(mouseevent.x(), mouseevent.y())
        scene_input.setType(SceneViewerInput.INPUT_EVENT_TYPE_MOTION_NOTIFY)
        if mouseevent.type() == QtCore.QEvent.Leave:
            scene_input.setPosition(-1, -1)
        
        self._scene_viewer.processInput(scene_input)
        
        # The viewport has been changed so update the OpenGL scene.
        self.updateGL()


