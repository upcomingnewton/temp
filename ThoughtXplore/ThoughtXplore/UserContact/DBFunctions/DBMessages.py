from ThoughtXplore.txMisc.DBFunctions.DBMessages import db_messages


def decode(result,rescode):
    if result == 1:
        return 'SUCCESS'
    elif result == 2:
        return 'Requested object already exists'
    else: 
        return db_messages[str(rescode)]
    
# insert function messages
db_messages.update({'601':'User registration failed. Please try again later, if problem persists, contact system administrator.',
               '602':'User registration failed. Error adding user to group. Please try again later, if problem persists, contact system administrator.',
               '603':'User registration failed. Error adding entry to logs.Please try again later, if problem persists, contact system administrator.',
               })

# update function messages
db_messages.update({
                    '2101':'user does not exist',
                    '2102':'user email or password is not correct',
                    '2103':'SYSTEM-ERROR.login type does not exist.Please report this error to your coordinator',
                    #2104 = insertion in login log table failed
                    '2104':'SYSTEM-ERROR. Error Generating login id.Please report this error to your coordinator',
                    })

