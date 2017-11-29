import os
import json
import codecs

def GetVideoName(inipath):
	data = open(inipath)
	next(data)
	InfoTip=data.readline().lstrip('InfoTip=')
	return InfoTip

def GetPartName(jsonpath):
	with codecs.open(jsonpath, 'r','utf8') as f:
		temp = json.loads(f.read())
		return temp['PartNo'],temp['PartName']

def GenerateFileName(PartNo,PartName,EXT):
	if PartName is None:
		num=int(PartNo)
		return '{0:0>2}{1}'.format(PartNo,EXT)
	else:
		return '{0:0>2}_{1}{2}'.format(PartNo,PartName,EXT)

def BConcat(videopath,outputpath):
	partlist = os.listdir(videopath)
	for partid in partlist:
		partdirpath = os.path.join(videopath,partid)
		if os.path.isdir(partdirpath):
			seglist = os.listdir(partdirpath)
			PartNo = ""
			PartName = ""
			EXT = ""
			filelistpath=os.path.join(partdirpath,'filelist.txt')
			segfilenamelist=[]
			for segid in seglist:
				segdirpath = os.path.join(partdirpath,segid)
				ext=os.path.splitext(segdirpath)[1]
				if ext=='.info':
					PartNo,PartName=GetPartName(segdirpath)
				if ext=='.flv':
					EXT=ext
					shortname = os.path.splitext(os.path.split(segdirpath)[1])[0];
					segind=int(shortname.split('_')[2]);
					segfilenamelist.append((segind,segdirpath))
					#print(segdirpath)
					#generate filelist.txt

			segfilenamelist=sorted(segfilenamelist, key=lambda segtuple: segtuple[0])
			f=open(filelistpath,'w')
			for item in segfilenamelist:
				f.write("file "+item[1].replace('\\','@').replace('@','\\\\')+"\n")
			f.close()
			OutputFileName=GenerateFileName(PartNo,PartName,EXT)
			outputfilepath=os.path.join(outputpath,OutputFileName.replace(' ','').replace(':','_'))
			command="ffmpeg -f concat -safe 0 -i \"{0}\" -c copy \"{1}\"".format(filelistpath,outputfilepath)
			# print(command)
			os.system(command)
		else:
			ext=os.path.splitext(partdirpath)[1]
			if ext=='.ini':
				#print(GetVideoName(partdirpath))
				newFoldName=GetVideoName(partdirpath)
				newFoldPath=os.path.join(outputpath,newFoldName)
				if !os.path.exists(newFoldPath):
					os.makedirs(newFoldPath)


if __name__ == '__main__':
	videopath=r'D:\Downloads\BilibiliDownload\16751135';
	outputpath=r'D:\Downloads\BilibiliDownload\16751135'
	BConcat(videopath,outputpath)
