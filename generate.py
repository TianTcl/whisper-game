# TianTcl - Whisper game - generator

import random

_subject    = ["ฉัน","คุณ","เขา","มัน","พวกเรา","พวกเขา","คน","ชาวบ้าน"]
ext_sub     = [None,"ที่สูงๆ","ที่กวาดถนนอยู่","ตรงนั้น","ในห้องนั้น"]
_verb       = ["กำลังวิ่ง","เดิน","คุยกัน","นอนอยู่"]
ext_verb    = [None,"อย่างรวดเร็ว","ช้าๆ","เสียงดังมาก"]
_object     = [None,"ในลู่วิ่ง","เรื่อง Python ","บนบาทวิถี","ใต้ต้นไม้"]
ext_obj     = [None,"ที่สนามกีฬา","ที่มีไม้ปกคลุม","ยักษ์ใหญ่"]

file_words = str(open(r"words\subject.txt","r"))
new_list = file_words.split("\n")
for word in new_list:
    _subject.append(word)
file_words = str(open(r"words\verb.txt","r"))
new_list = file_words.split("\n")
for word in new_list:
    _verb.append(word)
file_words = str(open(r"words\object.txt","r"))
new_list = file_words.split("\n")
for word in new_list:
    _object.append(word)
file_words = str(open(r"words\extend subject.txt","r"))
new_list = file_words.split("\n")
for word in new_list:
    _subject.append(word)
file_words = str(open(r"words\extend verb.txt","r"))
new_list = file_words.split("\n")
for word in new_list:
    _verb.append(word)
file_words = str(open(r"words\extend object.txt","r"))
new_list = file_words.split("\n")
for word in new_list:
    _object.append(word)

def make(_part):

    if _part == "subject":
        word = random.choice(_subject)
    elif _part == "verb":
        word = random.choice(_verb)
    elif _part == "object":
        word = random.choice(_object)
    elif _part == "ext subject":
        word = random.choice(ext_sub)
    elif _part == "ext verb":
        word = random.choice(ext_verb)
    elif _part == "ext object":
        word = random.choice(ext_obj)
    return word

def gen():
    parts =["subject","ext subject","verb","object","ext object","ext verb"]
    sentence = ""
    for part in parts:
        word = make(part)
        if word is not None:
            sentence += word
    return sentence
