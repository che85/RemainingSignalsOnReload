from weakref import WeakSet
import qt, slicer
from slicer.ScriptedLoadableModule import *

#
# RemainingSignalsAfterReload
#

class RemainingSignalsAfterReload(ScriptedLoadableModule):
  """Uses ScriptedLoadableModule base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """

  def __init__(self, parent):
    ScriptedLoadableModule.__init__(self, parent)
    self.parent.title = "RemainingSignalsAfterReload" # TODO make this more human readable by adding spaces
    self.parent.categories = ["Examples"]
    self.parent.dependencies = []
    self.parent.contributors = ["Christian Herz (SPL, BWH)"] # replace with "Firstname Lastname (Organization)"
    self.parent.helpText = """
    This module demonstrates issues of remaining signals after reloading the module. The UI element is connected to
    layout changes and will print a statements every time the layout got changed.

    After reloading this module, the call count of the underlying slot of the TextEdit which is connected to layout
    changes is resetted. For each time reloading this module, an additional signal/slot connections of the previously
    loaded UI element will remain and therefore will be called every time the layout changes.
    """
    self.parent.acknowledgementText = """
    This file was originally developed by Jean-Christophe Fillion-Robin, Kitware Inc.
    and Steve Pieper, Isomics, Inc. and was partially funded by NIH grant 3P41RR013218-12S1.
    """ # replace with organization, grant and thanks.

#
# RemainingSignalsAfterReloadWidget
#

class RemainingSignalsAfterReloadWidget(ScriptedLoadableModuleWidget):
  """Uses ScriptedLoadableModuleWidget base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """

  def onReload(self):
    # TODO: removing the comment # from the following line solves the problem
    self.widget.delete()
    ScriptedLoadableModuleWidget.onReload(self)

  def setup(self):
    ScriptedLoadableModuleWidget.setup(self)

    self.widget = qt.QWidget()
    rowLayout = qt.QHBoxLayout()
    self.widget.setLayout(rowLayout)
    self.widget.maximumHeight = 36

    self.callCountTextEdit = CustomTextEdit()
    self.callCountTextEdit.enabled = False

    rowLayout.addWidget(qt.QLabel("Number of layout changes (should be one at a time only)"))
    rowLayout.addWidget(self.callCountTextEdit)
    self.layout.addWidget(self.widget)
    self.layout.addStretch(1)


class CustomTextEdit(qt.QTextEdit):

  slotCallCount = 0

  @property
  def layoutManager(self):
    return slicer.app.layoutManager()

  def __init__ (self, text="", parent=None):
    qt.QTextEdit.__init__ (self, text, parent)
    self.setText(str(CustomTextEdit.slotCallCount))
    self.connectSignals()
    print "Resetting call count: %d" % CustomTextEdit.slotCallCount

  def connectSignals(self):
    self.destroyed.connect(self.onAboutToBeDestroyed)
    self.layoutManager.layoutChanged.connect(self.onLayoutChanged)

  def onAboutToBeDestroyed(self, obj):
    print "on destroyed"
    if self.layoutManager:
      self.layoutManager.layoutChanged.disconnect(self.onLayoutChanged)

  def onLayoutChanged(self):
    CustomTextEdit.slotCallCount += 1
    print "Layout changed. Call count: %d" % CustomTextEdit.slotCallCount
    self.setText(str(CustomTextEdit.slotCallCount))