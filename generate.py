# TianTcl - Whisper game - generator
import random
subject=["ฉัน","คุณ","เขา","มัน","พวกเรา","พวกเขา","คน","ชาวบ้าน"]
expand_subject=[None,"ที่สูงๆ","ที่กวาดถนนอยู่","ตรงนั้น","ในห้องนั้น"]
verb=["กำลังวิ่ง","เดิน","คุยกัน","นอนอยู่"]
epand_verb=[None,"อย่างรวดเร็ว","ช้าๆ","เสียงดังมาก"]
object=[None,"ในลู่วิ่ง","เรื่อง Python ","บนบาทวิถี","ใต้ต้นไม้"]
expand_object=[None,"ที่สนามกีฬา","ที่มีไม้ปกคลุม","ยักษ์ใหญ่"]
file_list=["subject","expand_subject","verb","object","expand_object","expand_verb"]
for filename in file_list:
    file_words = open(str("words/"+filename+".txt"),"r")
    if file_words.mode=="r":
        word=file_words.read().replace("\n",",").split(",")
        if filename == "subject":
            subject+=word
        elif filename == "verb":
            verb+=word
        elif filename == "object":
            object+=word
        elif filename == "extend_subject":
            expand_subject+=word
        elif filename == "extend_object":
            expand_object+=word
        elif filename == "extend_verb":
            expand_verb+=word
def make(_part):
    if _part == "subject":
        word = random.choice(subject)
    elif _part == "verb":
        word = random.choice(verb)
    elif _part == "object":
        word = random.choice(object)
    elif _part == "expand subject":
        word = random.choice(expand_subject)
    elif _part == "expand verb":
        word = random.choice(epand_verb)
    elif _part == "expand object":
        word = random.choice(expand_object)
    return word
parts =["subject","expand subject","verb","object","expand object","expand verb"]
def gen():
    sentence = ""
    for part in parts:
        word = make(part)
        if word is not None:
            sentence += word
    return sentence