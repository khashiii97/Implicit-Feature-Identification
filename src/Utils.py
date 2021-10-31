import string
from hazm import *
english_letters = list(string.ascii_lowercase) + list(string.ascii_uppercase) + ['0','1','2','3','4','5','6','7','8','9'] + ['+','×',':']
import re
punctuations = ['؟','!','.',',','،','?',')','(',')','(','\\','\n']
bad_words_with_heh = []
with open('auxiliary-files/noun-hehs.txt', 'r', encoding='utf-8') as in_file:
    strings = in_file.read().split("\n")
    for i in range(len(strings)):
        bad_words_with_heh.append(strings[i])
with open('auxiliary-files/heh-faults.txt', 'r', encoding='utf-8') as in_file:
    strings = in_file.read().split("\n")
    for i in range(len(strings)):
        bad_words_with_heh.append(strings[i])
with open('auxiliary-files/verb-hehs.txt', 'r', encoding='utf-8') as in_file:
    strings = in_file.read().split("\n")
    for i in range(len(strings)):
        bad_words_with_heh.append(strings[i])
bad_words_with_ist = []
with open('auxiliary-files/ist.txt', 'r', encoding='utf-8') as in_file:
    strings = in_file.read().split("\n")
    for i in range(len(strings)):
        bad_words_with_ist.append(strings[i])
bad_words_with_ast = []
with open('auxiliary-files/asts.txt', 'r', encoding='utf-8') as in_file:
    strings = in_file.read().split("\n")
    for i in range(len(strings)):
        bad_words_with_ast.append(strings[i])
adverbs = []
with open('auxiliary-files/adverbs.txt', 'r', encoding='utf-8') as in_file:
    adverbs = in_file.read().split("\n")

verbs = []
with open('auxiliary-files/verbs.txt', 'r', encoding='utf-8') as in_file:
    verbs = in_file.read().split("\n")

bad_words_with_yeh = []
with open('auxiliary-files/yeh.txt', 'r', encoding='utf-8') as in_file:
    strings = in_file.read().split("\n")
    for i in range(len(strings)):
        bad_words_with_yeh.append(strings[i])
def remove_word_from_opinion(word,opinion):
    word_to_be_removed = word
    if word + ' ' in opinion:
        word_to_be_removed = word + ' '
    if ' ' + word in opinion:
        word_to_be_removed = ' ' + word
    if ' ' + word + ' ' in opinion:
        word_to_be_removed = word + ' '
    opinion = opinion.replace(word_to_be_removed,'')
    while opinion.endswith(' '):
        opinion = opinion[:-1]
    return opinion
def change_opinion(opinion,condition,replacement):
    if opinion == condition:
        return replacement
    return opinion
def opinion_root_extractor(opinion,replace_word = True):
    before1 = opinion
    def print_op(before):
        if before == before1:
            print(opinion)
            print("oooo")
    def print_before(op):
        if op == opinion:
            print(before1)
            print('bbb')
    opinion = re.sub(' +', ' ', opinion)
    opinion = opinion.replace('ي', 'ی')
    opinion = opinion.replace('ی', 'ی')
    opinion = opinion.replace('ً','')
    opinion = opinion.replace('ء','')
    opinion = opinion.replace('\u200c', '')
    opinion = opinion.replace('آ', 'ا')
    opinion = opinion.replace('ارزون', 'ارزان')
    opinion = opinion.replace('گرون', 'گران')
    opinion = opinion.replace('کوچیک', 'کوچک')
    opinion = opinion.replace('روون', 'روان')
    opinion = opinion.replace('اسون', 'اسان')
    opinion = opinion.replace('ئ','ی')
    opinion = opinion.replace(' یه ', ' یک ')
    opinion = opinion.replace('یه ', 'یک ')
    opinion = opinion.replace('با حال', 'باحال')
    opinion = opinion.replace('با کیفیت','باکیفیت')
    opinion = opinion.replace('یک کم', 'یکم')
    opinion = opinion.replace('اومده', 'امد')
    opinion = opinion.replace('اومد', 'امد')
    opinion = opinion.replace('امده', 'امد')
    for p in punctuations + ['-'] +  ['؛']:
        opinion = opinion.replace(p, ' ')
    for w in opinion:
        if w in english_letters:
            opinion = opinion.replace(w,' ')
    opinion = re.sub(' +', ' ', opinion)
    before = opinion
    if 'فوق العاده ست' in opinion:
        opinion = opinion.replace('فوق العاده ست' , 'فوق العاده')
    for adverb in adverbs:
        if len(adverb.split(' ')) == 1:
            if adverb in opinion.split(' '):
                if not opinion.endswith(adverb):
                    opinion = remove_word_from_opinion(adverb, opinion)
        elif adverb in opinion:
            opinion = remove_word_from_opinion(adverb, opinion)


    if 'در حد ' in opinion:
        opinion = remove_word_from_opinion('در حد', opinion)
    if 'کمی' in opinion.split(' '):
            if not opinion.endswith('کمی'):
                opinion = remove_word_from_opinion('کمی', opinion)
            else:
                opinion = opinion[: -1]
    for verb in verbs:
        if verb in opinion.split(' '):
            opinion = remove_word_from_opinion(verb,opinion)
    nouns_with_tar = ['شاتر','باتری','دسترس' ,'میلیمتر','در دسترس' ,'استریو' ,'کنتراست']
    bad_tars = ['بهتر', 'برتر', 'بيشتر']
    endings = ['اس' ,'ها' ,'شو' ,'هاست']
    words_with_yeh = ['کاف' ,'عال','کاربرد','صیقل','قو','به خوب','طولان','روان','دوست داشتن','طبيع','اس ب','معمول','انقلاب','پیاپ'
                      'پیاپ','صرفه‌ جو','گرفتگ','منطق','مبتد','فارس','بعد','جزئ','غن','اصول','پشتيبان','دست نيافتن' ,'راض','تازگ' ,'دوستداشتن' ,'مثالزدن','مثال زدن','اساس','تکنولوژ','تکرار',
                      'جد','دوست داشتن','سادگ','سفارش','صرفه جوی','طبیع','عاد','پشتیبان','قدیم','جزی','اصل','جانب','پیاپ',]
    words_with_sh = ['افزایش','استایلیش','بیش','چرخش','بخش' ,'خش','لرزش','کاهش' ,'ارزش',]
    words_with_ash = ['زیباش' ,'بالاش']
    for word in bad_words_with_heh:
        if word in opinion.split(' '):
            opinion = opinion.replace(word,word[:-1])
    for word in bad_words_with_ist:
        if word in opinion.split(' ') and word != 'ساده ایست' and word not in ['کافیست','عالیست','داشتنیست']:
            opinion = opinion.replace(word,word[:-3])
        elif word == 'ساده ایست':
            opinion = opinion.replace(word, word[:-5])
        elif word in ['کافیست','عالیست','داشتنیست']:
            opinion = opinion.replace(word, word[:-2])
    for word in bad_words_with_ast:
        if word in opinion.split(' '):
            opinion = opinion.replace(word,word[:-2])
    for word in bad_words_with_heh:
        if word in opinion.split(' '):
            opinion = opinion.replace(word,word[:-1])
    for word in bad_words_with_yeh:
        if word in opinion.split(' '):
            opinion = opinion.replace(word,word[:-1])
    while opinion.endswith(' '):
        opinion = opinion[:-1]
    if opinion.endswith('های') and not opinion.startswith('حرف') and not opinion.startswith('خیرهکننده') :
        opinion = opinion[:-3]

    if opinion.endswith('ایه') and not opinion.startswith('حرف'):
        opinion = remove_word_from_opinion('ایه' , opinion)
    words_with_ay1 = ['بالای', 'زیبای', 'غول آسای', 'مزایای', ]
    words_with_ay2 = ['حرفه ای' , 'حرفهای']

    if opinion.endswith('ای') :
        ay_flag = False
        for word in words_with_ay1:
            if opinion.endswith(word):
                opinion = opinion[:-1]
                ay_flag = True
                break
        if ay_flag == False:
            for word in words_with_ay2:
                if opinion.endswith(word):
                    ay_flag = True
                    break
            if ay_flag == False:
                opinion = opinion[:-2]
                while opinion.endswith(' '):
                    opinion = opinion[:-1]




    if opinion.endswith('ی'):
        y_flag = False
        for word in words_with_yeh:
            if opinion.endswith(word + 'ی'):
                y_flag = True
                break
        for word in words_with_ay2:
            if opinion.endswith(word):
                y_flag = True
                break
        if y_flag == False:
            opinion = opinion[:-1]
    if opinion.endswith('ی'): # this time for removing یی in words like زیبایی
        y_flag = False
        for word in words_with_yeh:
            if opinion.endswith(word + 'ی'):
                y_flag = True
                break
        for word in words_with_ay2:
            if opinion.endswith(word):
                y_flag = True
                break
        if y_flag == False:
            opinion = opinion[:-1]

    if 'فوق العادست' in opinion:
        opinion = opinion.replace('فوق العادست' , 'فوق العاده')
    if 'فوقالعادست' in opinion:
        opinion = opinion.replace('فوقالعادست' , 'فوق العاده')
    if 'فوق العادس' in opinion:
        opinion = opinion.replace('فوق العادس' , 'فوق العاده')
    if 'کنندست' in opinion:
        opinion = opinion.replace('کنندست' , 'کننده')
    if 'پدیدست' in opinion:
        opinion = opinion.replace('پدیدست' , 'پدیده')


    for ending in endings:
        if opinion.endswith(ending) and opinion not in ['اساس' ,'حساس']:
            opinion = opinion[0: -1 * len(ending)]
            break

    if 'ترین' in opinion:
        flag = False
        for tar in bad_tars:
            if tar in opinion:
                flag = True
                break
        if flag != True:
            if opinion.index('ترین') + 3 > len(opinion) - 4:
                opinion = opinion[:opinion.index('ترین')]
        else:
            if opinion.index('ترین') + 3 > len(opinion) - 4:
                opinion = opinion[:opinion.index('ترین') + 2]

    if 'تر' in opinion and 'ترین' not in opinion and ('گسترده' not in opinion and 'اینترنت' not in opinion and 'استریو' not in opinion and 'کنتراست' not in opinion):
        flag = False
        for tar in bad_tars + nouns_with_tar :
            if tar in opinion:
                flag = True
                break
        if flag != True:
            opinion = opinion[:opinion.index('تر')]
        elif opinion != 'در دسترس':
            opinion = opinion[:opinion.index('تر') + 2]
    if opinion.endswith('اش'):
        ash_flag = False
        for word in words_with_ash:
            if opinion.endswith(word):
                ash_flag = True
                break
        if ash_flag == False:
            opinion = opinion[:-2]

    if opinion.endswith('ش'):
        sh_flag = False
        for word in words_with_sh:
            if opinion.endswith(word):
                sh_flag = True
                break
        if sh_flag == False:
            opinion = opinion[:-1]
    while opinion.endswith(' '):
        opinion = opinion[0:-1]
    opinion = opinion.replace('فوق العاده','فوقالعاده')
    if 'فوقالعاده' in opinion and len(opinion.split(' ')) > 1 and opinion.endswith('فوقالعاده') == False:
        opinion = remove_word_from_opinion('فوقالعاده',opinion)
    # if opinion == 'زیباتر':
    #     print(before)
    #     print("+++")

    if opinion == 'س خ':
        opinion = 'خوب'
    if opinion == 'بزرگو':
        opinion = 'بزرگ'
    # if opinion == 'ایه':
    #     print(before)
    #     print("++++++++")
    if opinion == '' and 'HD' in before1:
        opinion = 'HD'
    # if before1 == 'کاملا حساس':
    #     print(opinion)


    opinion = opinion.replace(' ی ',' ')
    if 'شدم' in opinion:
        opinion = remove_word_from_opinion(opinion=opinion,word='شدم')
    if 'نبوده' in opinion:
        opinion = remove_word_from_opinion(opinion=opinion,word='نبوده')
    if 'مطلوب' in opinion:
        opinion = opinion.replace('مطلوب','خوب')
    if 'قدرتن' in opinion:
        opinion = opinion.replace('قدرتن', 'قدرت')
    if 'بالاتر' in opinion:
        opinion = opinion.replace('بالاتر', 'بالا')


    if opinion.endswith('اند'):
        opinion = opinion[:-3]
    while opinion.endswith(' '):
        opinion = opinion[0:-1]
    opinion = change_opinion(opinion,'اذیتم','اذیت')
    opinion = change_opinion(opinion,'ارتقا یافته','ارتقا')

    opinion = change_opinion(opinion, 'خوبتون', 'خوب')

    opinion = change_opinion(opinion, 'خوشم میاد', 'خوشم امد')
    opinion = change_opinion(opinion, 'کیفیتی', 'کیفیت')
    opinion = change_opinion(opinion, 'خوشم میاد', 'خوشم امد')
    opinion = change_opinion(opinion, 'خوشم میاد', 'خوشم امد')
    opinion = change_opinion(opinion, 'راضیم', 'راضی')
    opinion = change_opinion(opinion, 'راضی ام', 'راضی')
    opinion = change_opinion(opinion, 'داره', 'دارد')
    opinion = opinion.replace('دکمهی', 'دکمه')
    opinion = change_opinion(opinion, 'راضیام', 'راضی')

    opinion = change_opinion(opinion, 'عــالـیـــه', 'عالی')
    opinion = change_opinion(opinion, 'عملکردی', 'عملکرد')
    opinion = change_opinion(opinion, 'غولیههههههه', 'غول')
    opinion = change_opinion(opinion, 'فوقالعاد', 'فوقالعاده')
    opinion = change_opinion(opinion, 'قابله', 'قابل')
    opinion = change_opinion(opinion, 'قدرمند', 'قدرتمند')

    opinion = change_opinion(opinion, 'محشرن', 'محشر')

    opinion = change_opinion(opinion, 'معرک', 'معرکه')

    opinion = change_opinion(opinion, 'نمیمونه', 'نمیماند')
    opinion = change_opinion(opinion, 'نداره', 'ندارد')
    opinion = change_opinion(opinion, 'همیشگ', 'همیشه')
    opinion = change_opinion(opinion, 'ویژه ا', 'ویژه')
    opinion = change_opinion(opinion, 'پرفرو', 'پرفروش')
    opinion = opinion.replace('اپلیکشن', 'اپلیکیشن')
    opinion = change_opinion(opinion, 'یرهکنند', 'خیرهکننده')

    if replace_word:
        opinion = change_opinion(opinion, 'ارزان قیمت', 'ارزان')
        opinion = change_opinion(opinion, 'ارزان کردن', 'ارزان')
        opinion = change_opinion(opinion, 'افزایش داد', 'افزایش')
        opinion = change_opinion(opinion, 'جالباند', 'جالب')
        opinion = change_opinion(opinion, 'حال مید', 'باحال')
        opinion = change_opinion(opinion, 'خوش استیل', 'استایلیش')
        opinion = change_opinion(opinion, 'کیفیت زیاد', 'کیفیت بالا')
        opinion = change_opinion(opinion, 'کیفیت عالی', 'کیفیت فوقالعاده')
        opinion = change_opinion(opinion, 'قیمت پایین', 'قیمت ارزان')
        opinion = change_opinion(opinion, 'معتبرتر', 'معتبر')
        opinion = change_opinion(opinion, 'قیمت پایین', 'قیمت ارزان')
        opinion = change_opinion(opinion, 'سبک وزن', 'سبک')
        opinion = change_opinion(opinion, 'سرعت بالا', 'سرعت زیاد')
        opinion = change_opinion(opinion, 'سرعت بیش', 'سرعت زیاد')
        opinion = change_opinion(opinion, 'صدای بالا', 'صدای بلند')





    if 'داغ' in opinion.split(' '):
        opinion = 'داغ'










    opinion = opinion.replace(' ','')
    if opinion =='منحصربهفرده' :
        opinion = 'منحصربهفرد'
    if opinion =='لذتبخشه' :
        opinion = 'لذتبخش'
    if opinion =='جابهجاییش' :
        opinion = 'جابهجایی'






    return opinion

def extract_aspect_root(aspect):
    before = aspect
    for p in  ['0','1','2','3','4','5','6','7','8','9'] + ['+','×',':']+ ['-'] +  ['؛'] + ['_']:
        aspect = aspect.replace(p, ' ')
    aspect = re.sub(' +', ' ', aspect)
    aspect = aspect.replace('ي', 'ی')
    aspect = aspect.replace('ی', 'ی')
    aspect = aspect.replace('ً', '')
    aspect = aspect.replace('ء', '')
    aspect = aspect.replace('\u200c', '')
    aspect = aspect.replace('آ', 'ا')
    aspect = aspect.replace('ارزون', 'ارزان')
    aspect = aspect.replace('گرون', 'گران')
    aspect = aspect.replace('کوچیک', 'کوچک')
    aspect = aspect.replace('روون', 'روان')
    aspect = aspect.replace('اسون', 'اسان')
    aspect = aspect.replace('ئ', 'ی')
    aspect = aspect.replace('ى', 'ی')
    aspect = aspect.replace(' یه ', ' یک ')
    aspect = aspect.replace('یه ', 'یک ')
    aspect = aspect.replace('با حال', 'باحال')
    aspect = aspect.replace('با کیفیت', 'باکیفیت')
    aspect = aspect.replace('یک کم', 'یکم')
    aspect = aspect.replace('اومده', 'امد')
    aspect = aspect.replace('اومد', 'امد')
    aspect = aspect.replace('امده', 'امد')
    aspect = aspect.replace('خریدن', 'خرید')
    aspect = aspect.replace('اپلیکشن', 'اپلیکیشن')
    aspect = aspect.replace('تایپ کردن', 'تایپ')
    aspect = aspect.replace('پیکسلی', 'پیکسل')
    aspect = aspect.replace('براقی', 'براق')
    aspect = aspect.replace(' ی', '')
    if not aspect.endswith('دهی') and ' دهی' not in aspect:
        aspect = aspect.replace('هی','ه')
    aspect = aspect.replace(' ', '')
    if aspect =='جابهجاییش' :
        aspect = 'جابهجایی'

    return aspect
