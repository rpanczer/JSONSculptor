import json
var currentType
var currentTextInput

if currentType = "textInput"
    if currentTypicalText is null then
        currentTypicalText = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

    currentTextInput = dict([('type', 'textInput'), ('label', currentLabel), ('id', currentId), ('ctype', currentDataType),
                             ('prompt', currentPrompt), ('editable',currentEditable), ('required', currentRequired),
                             ('percentWidth',currentPercentWidth), ('typicalText', currentTypicalText), ('default', currentDefault)])

if currentType = "comboBox"
    if currentTypicalText is null then
        currentTypicalText = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

    currentComboBox = dict([('type', 'textInput'), ('label', currentLabel), ('id', currentId), ('ctype', currentDataType),
                             ('prompt', currentPrompt), ('editable',currentEditable), ('required', currentRequired),
                             ('percentWidth',currentPercentWidth), ('typicalText', currentTypicalText), ('default', currentDefault)])