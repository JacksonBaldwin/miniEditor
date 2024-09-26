import os
current_file = ''
current_path = ''
current_content = ''

def loadState(): #parse previous saved state, load previous file if needed
    global current_file
    global current_content
    global current_path
    st = open('./state.txt','r')
    st_read = st.read()
    state = []
    save = ''
    for i in range(0,len(st_read)):
        if st_read[i] == '\n':
            state.append(save)
            save = ''
        else:
            save += st_read[i]
    state.append(save)
    if state[0] == 'none':
        return 0 #zero as in no action taken
    elif state[0] == 'open':
        try:
            current_file = open(state[1],'r')
            current_path = state[1]
            current_content = current_file.read()
            return 1 #action complete
        except:
            return 2 #action failed
    st.close()

def saveState(): #done on exit, closes current file
    global current_path
    st = open('./state.txt','w')
    if current_path != "":
        st.write('open\n'+str(current_path))
    else:
        st.write('none')
    current_file.close()
    saveFile(current_content)

def saveFile(text):
    global current_path
    try:
        sf = open(current_path,'w')
        sf.write(text)
        sf.close()
        return 0
    except:
        return 1



#on run
loadst = loadState()
if loadst == 2:
    print('error loading program state, relaunch the program')
    saveState() # error probably caused by missing state file, this should fix

