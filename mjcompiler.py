"""

~~~~~~~~~~~~~~~~~~~Operators used!~~~~~~~~~~~~~~~~~~~~~~~~
<aaow> = increment the value of the pointer in the array.
<hee hee> = decrement the value of the pointer in the array.
<i want you back> = decrement operator for the pointer position ptr--
<moonwalk> = increment operator for the operator ptr++
<michael> = prints the 51 byte character array, which is the sole memory space in the
	    entire program.
<this is it> = prints the value of the current pointer in the array.
<xscape> = use to terminate the loop
<give in to me> = used to take in a 1 byte input
<wanna be starting something> = puts 0 in all positions of the 51 byte array.
<history> = prints contents of pointer-1 in the array.

~~~~~~~~~~~~~~~~~~~Random shit~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
<annie are you ok ?> = 
<king of pop> = 
<dangerours> = 
<thriller> = 
<who is it?>
<billie jean> =
<ABC> = 
<scream> = 
<blood on the dance floor>
<don't stop till you get enough> =

Anything not withing the angular brackets, is a comment.
"""

lookup=['<aaow>','<hee hee>','<i want you back>','<moonwalk>','<michael>','<this is it>','<xscape>','<give in to me>','<wanna be starting something>','<history>']
import sys
from time import sleep
michael=[0]*51
ptr=0
s="""
---::::----.............---......-..........---/NNdho+/++smdddmNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
---::::--..........````............``.`````:-.-:ds``....-o/--::/sysdNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
----::--.....`.````````.....````.``````````:```.yo`````.:```````s.-+dMNMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
----::--..-.``..```````.....````.``````````:```///``````    ````.o:.-ymNNMMMMMMMMMMMMMMMMMMMMMMMMMMM
-.---:---...```````````......``````````````-```o/``````    ```````///y+yhdNMMMMMMMMMMMMMMMMMMMMMMMMM
-.------...````````````.....```````````````.``-.:+.````   ````````-do:::+ooshssymMMMMMMMMMMMMMMMMMMM
...-----...````````````.....``````````````.--.```.+```   ```````./ho::::-::oso://ddymMMMMMMMMMMMMMMM
...-----...````````````....`````````````.:.`````-+-`.`    `````/o:`+s:-:::o/y+::+dyohNMMMMMMMMMMMMMM
..------....``````````......````````````:.````//-`./+:``` ````-o----:++/+ooy+:/sdyoydNMMMMMMMMMMMMMM
---::::--....`````````......`````````````-````..---+ddd+.`` ````.-:/oyshh++//hdo::+dmNMMMMMMMMMMMMMM
--::::----...``````````....``````````````.--.`````.+oshds-```.:ohmNNNNNMMNNmmd/:--:+hNMMMMMMMMMMMMMM
--:::::---.....```````......````````````````.:.`.:smmhhhy/``.-/ossssoshmysshmNyo/:+ss/dMMMMMMMMMMMMM
----::::---......`````......`````````````````-.```.oh//+o. `-://oymmhddmdhyyssyysho:::/NMMMMMMMMMMMM
...-----....``````````......``````````````````````..::-.` .://:-:+ydmohNMMMmho/::/---:+mNMMMMMMMMMMN
---::---...........``.......```````````````````````      `:/::-.`..:ooyhdmds/-.....--:omMMMMMMmdmhys
..------...........```.......``````````````````````    `.-----..`````.----..````...--:yNMMMNmhyys+os
...---..............`........`````````````````````  ```..---...``    `` ````````...-:+mMMMdooyhyo//+
...--..................--......`````````````````````.:::/:..---.``   `````````...--:/oNMMd//:+ysoso+
...--..................--......``.`````````````````` ..:oo/-::-.```````.``....----::/oNMd++::+o+os+y
...---.................--........```````````````...`````.......``````......-----::://+ymy+/+so+oosyN
...---.................--.......`.....`````````........```.......```..---------:::::+oo+o++////+sdMM
..-----................--.......`.....``...........:+o++///::-----....--:--------::/+o+oooy///ohMMMM
..-----................--.......`.`........`....---...:////+osyyy+---------------:://+ooshNNMMMMMMMM
..-----................--...................+ysydmm..----:::/+++/:--------------::://osshdmMMMMMMMMM
..-----................--...................os::hsd:.-://:------.--::::::-----::///++syddmNMMMMMMMMM
..-----................--..................../ydNNm+`....----------::////::::://++osyddddmNMMMMMMMMM
..-----...............---...............-:/+shmMMMMy``.`````.....--://///////++osyhdddhhhmMMMMMMMMMM
..-----...............-..........-/+sydmNMMMMMMMMMMM+---..---.--:/++oooossssyyhhddhhyyyyhmMMMMMMMMMM
..------..............---..-/oydNMMMMMMMMMMMMMMMMMMMMdhhyssoooossyyyyyhhhhyyyyyyhyysssyhmMMMMMMMMMMM
.--:----.............-:oydmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy///+sssooooooossssssoooosmMNMMMMMMMMMMM
..--------.......-/osdNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM+::::/oo++//++oossssooooohMNNNNmMMMMMMMM
..-------......:yNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN/:---:/+o+/++oooossooooosymNNMMdmMMMMMMM
..-------....-sNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMyoo::::::/+++oooooossoooossyhhdd:-oMMMMMMM
.-----------+dMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM/:ms/:::::/+++ooooooooooossyhhhy-:hMMMMMMM
..---------/NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMs.odo::::://++o+oooooooossyyhhy/:/hNMMMMMM
"""
print s
#sleep(5)
print 'Hello, I am MJ. I love you ...'
print '...'
print '...'
print '...'
print 'Let me compile the program for you! '
print 'hee hee hee '
print 'Compilation begins!'
print '____________________________________________________________________________________________________________'
source_filename=str(sys.argv[1])
if not source_filename[-3:]=='.mj':
    print 'Please check the source file, it should be an appropriate mjlang file.'
    sys.exit()

f=open(source_filename,'r')
mjlang=f.read()
mjlang.replace(' ','')
mjlang.replace('\n','')
mjlang.replace('\t','')

"""
Now we start reading the source file text mjlang
"""
n=len(mjlang)
i=0
while i<n:
    #start of a keyword/operator
    if mjlang[i]=='<':
	tmp=''
	while i<n and not mjlang[i]=='>':
	    tmp+=mjlang[i]
	    i+=1
	if i==n:
	    break
	tmp+=mjlang[i]
	if tmp not in lookup:
	    print 'Unidentified symbol %s at %d character.' % (tmp,i+1)
	    break
	else:
	    if tmp=='<aaow>':
		michael[ptr]=(michael[ptr]+1)%128
	    elif tmp=='<hee hee>':
		michael[ptr]=(michael[ptr]-1)%128
	    elif tmp=='<i want you back>':
		ptr-=1
	    elif tmp=='<moonwalk>':
		ptr+=1
	    elif tmp=='<this is it>':
		sys.stdout.write(str(unichr(michael[ptr])))
	    elif tmp=='<xscape>':
		break
	    elif tmp=='<give in to me>':
		michael[ptr]=ord(str(sys.stdin.read(1)))
	    elif tmp=='<history>':
		sys.stdout.write(michael[(ptr-1)%128])
	    elif tmp=='<wanna be starting something>':
		for i in xrange(51):
		    michael[i]=0
	    else:
		tmp=[]
		for j in xrange(51):
		    tmp.append(str(unichr(michael[j])))
		print ''.join(tmp)
    i+=1