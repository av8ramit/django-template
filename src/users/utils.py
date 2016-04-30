'''Forms page for the users django template module.'''

def upload_location(instance, filename):
    '''Define the location in the media directory where and how to store the file.'''
    return "%s/%s" % (instance.username, filename)
