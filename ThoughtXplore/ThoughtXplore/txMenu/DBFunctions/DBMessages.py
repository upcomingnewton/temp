from ThoughtXplore.txMisc.DBFunctions.DBMessages import db_messages


def decode(result,rescode):
    try:
        if result == -1:
            return 'Exception occoured at Database Helper class for this model'
        if result == 1:
            return 'Success'
        elif result == 2:
            return 'Specified object already exists. ' + db_messages[str(rescode)]
        else: 
            return db_messages[str(rescode)]
    except:
        pass
    
# insert function messages
db_messages.update({
                    '2401':'Menu with these parameters already exist.',
                    '2402':'Menu Insertion failed in Menu table',
                    })