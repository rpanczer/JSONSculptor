import json
var currentType
var currentTextInput
# version 1.001
if currentType = "textInput"
    if currentTypicalText is null then
        currentTypicalText = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

    currentTextInput = dict([('type', 'textInput'), ('label', currentLabel), ('id', currentId), ('ctype', currentDataType),
                             ('prompt', currentPrompt), ('editable',currentEditable), ('required', currentRequired),
                             ('percentWidth',currentPercentWidth), ('typicalText', currentTypicalText), ('default', currentDefault)])
    currentObject = currentTextInput

if currentType = "mTextInput"
    if currentTypicalText is null then
        currentTypicalText = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

    currentMTextInput = dict([('type', 'mTextInput'), ('label', currentLabel), ('id', currentId), ('ctype', currentDataType),
                             ('prompt', currentPrompt), ('editable',currentEditable), ('required', currentRequired),
                             ('percentWidth',currentPercentWidth), ('typicalText', currentTypicalText), ('default', currentDefault)])
    currentObject = McurrentTextInput

if currentType = "comboBox"
    if currentTypicalText is null then
        currentTypicalText = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

    currentComboBox = dict([('type', 'comboBox'), ('label', currentLabel), ('id', currentId), ('ctype', currentDataType),
                             ('prompt', currentPrompt), ('editable',currentEditable), ('required', currentRequired),
                             ('percentWidth',currentPercentWidth), ('typicalText', currentTypicalText), ('default', currentDefault)])
    currentObject = currentComboBox

if currentType = "mComboBox"
    if currentEditable is null then
        currentEditable = 'true'

    currentMComboBox = dict([('type', 'mComboBox'), ('label', currentLabel), ('id', currentId), ('ctype', currentDataType),
                             ('editable',currentEditable), ('required', currentRequired),
                             ('addEntries',currentaddEntries), ('dataProvider', currentDataprovider), ('init', currentInit)])
    currentObject = currentMComboBox

if currentType = "checkBoxBtn"

    currentcheckBoxBtn = dict([('type', 'checkBoxBtn'), ('label', currentLabel), ('id', currentId), ('ctype', 'VARCHAR(MAX)'),
                             ('visible',currentVisible), ('required', currentRequired),
                             ('percentWidth', '100'), ('linesHigh', currentLinesHigh)])
    currentObject = currentcheckBoxBtn

# Convert Labels to dictionary
if currentType = "label"
    if alert is null then
        alert = 'false'

    currentLabel = dict([('type', 'label'), ('label', currentLabel)])
    currentObject = currentLabel

if currentType = "inspector"

    currentInspector = dict([('type', 'inspector'), ('label', 'Inspector'), ('id','_inspector', ('ctype','VARCHAR(100)'),
                            ('percentWidth','50'), ('spacer','0'), ('default',''))])
    currentObject = currentInspector

if currentType = "timeStamp"

    currentTimestamp = dict([('type', 'timeStamp'), ('label', 'Last Modified'), ('id','_timestamp'), ('ctype','DATETIME'),
                            ('percentWidth','50'), ('spacer','0'), ('default','date(now)')])
    currentObject = currentTimestamp

if currentType = "math"
    if currentFilename is null then
        currentFilename = ""
    currentMath = dict([('type', 'math'), ('filename', currentFilename), ('vars',''), ('sql',''),
                            ('code','')])
    currentObject = currentMath

if currentType = "pictures"
    if currentLabel is null then
        currentLabel = "Pictures"
    if currentID is null then
        currentID = "pictures"
    currentcheckBoxBtn = dict([('type', 'pictures'), ('label', currentLabel), ('id', currentId), ('ctype', 'VARCHAR(255)'),
                             ('picName',currentPicName), ('required', currentRequired), ('stamp',''),
                             ('percentWidth', '100'), ('requiredNumber', currentReqNumber)])
    currentObject = currentcheckBoxBtn

json.JSONEncoder(currentObject)