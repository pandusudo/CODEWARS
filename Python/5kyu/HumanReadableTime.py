def make_readable(seconds):
    hours =  str(seconds // 3600) if seconds // 3600 > 9 else '0' + str(seconds // 3600)
    minutes = str((seconds % 3600) // 60) if (seconds % 3600) // 60 > 9 else '0' + str((seconds % 3600) // 60)
    secs = str((seconds % 3600) % 60) if (seconds % 3600) % 60 > 9 else '0' + str((seconds % 3600) % 60) 
    return hours+':'+minutes+':'+secs
