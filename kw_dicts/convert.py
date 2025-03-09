import re

romaji_to_kana = {
    '-': 'ー',
    'a': 'あ', 'i': 'い', 'u': 'う', 'e': 'え', 'o': 'お', 'ye': 'いぇ', 'wha': 'うぁ',
    'whi': 'うぃ', 'whe': 'うぇ', 'who': 'うぉ', 'wyi': 'ゐ', 'wye': 'ゑ', 'xa': 'ぁ',
    'xi': 'ぃ', 'xu': 'ぅ', 'xe': 'ぇ', 'xo': 'ぉ', 'ka': 'か', 'ki': 'き', 'ku': 'く',
    'ke': 'け', 'ko': 'こ', 'kya': 'きゃ', 'kyi': 'きぃ', 'kyu': 'きゅ', 'kye': 'きぇ',
    'kyo': 'きょ', 'qya': 'くゃ', 'qyu': 'くゅ', 'qyo': 'くょ', 'qwa': 'くぁ', 'qwi': 'くぃ',
    'qwu': 'くぅ', 'qwe': 'くぇ', 'qwo': 'くぉ', 'ga': 'が', 'gi': 'ぎ', 'gu': 'ぐ',
    'ge': 'げ', 'go': 'ご', 'gya': 'ぎゃ', 'gyi': 'ぎぃ', 'gyu': 'ぎゅ', 'gye': 'ぎぇ',
    'gyo': 'ぎょ', 'gwa': 'ぐぁ', 'gwi': 'ぐぃ', 'gwu': 'ぐぅ', 'gwe': 'ぐぇ', 'gwo': 'ぐぉ',
    'xka': 'ゕ', 'xke': 'ゖ', 'sa': 'さ', 'si': 'し', 'su': 'す', 'se': 'せ', 'so': 'そ',
    'sya': 'しゃ', 'syi': 'しぃ', 'syu': 'しゅ', 'sye': 'しぇ', 'syo': 'しょ', 'swa': 'すぁ',
    'swi': 'すぃ', 'swu': 'すぅ', 'swe': 'すぇ', 'swo': 'すぉ', 'za': 'ざ', 'zi': 'じ',
    'zu': 'ず', 'ze': 'ぜ', 'zo': 'ぞ', 'zya': 'じゃ', 'zyi': 'じぃ', 'zyu': 'じゅ', 'zye': 'じぇ',
    'zyo': 'じょ', 'ta': 'た', 'ti': 'ち', 'tu': 'つ', 'te': 'て', 'to': 'と', 'tya': 'ちゃ',
    'tyi': 'ちぃ', 'tyu': 'ちゅ', 'tye': 'ちぇ', 'tyo': 'ちょ', 'tsa': 'つぁ', 'tsi': 'つぃ',
    'tse': 'つぇ', 'tso': 'つぉ', 'tha': 'てゃ', 'thi': 'てぃ', 'thu': 'てゅ', 'the': 'てぇ',
    'tho': 'てょ', 'twa': 'とぁ', 'twi': 'とぃ', 'twu': 'とぅ', 'twe': 'とぇ', 'two': 'とぉ',
    'da': 'だ', 'di': 'ぢ', 'du': 'づ', 'de': 'で', 'do': 'ど', 'dya': 'ぢゃ', 'dyi': 'ぢぃ',
    'dyu': 'ぢゅ', 'dye': 'ぢぇ', 'dyo': 'ぢょ', 'dha': 'でゃ', 'dhi': 'でぃ', 'dhu': 'でゅ',
    'dhe': 'でぇ', 'dho': 'でょ', 'dwa': 'どぁ', 'dwi': 'どぃ', 'dwu': 'どぅ', 'dwe': 'どぇ',
    'dwo': 'どぉ', 'xtu': 'っ', 'na': 'な', 'ni': 'に', 'nu': 'ぬ', 'ne': 'ね', 'no': 'の',
    'nya': 'にゃ', 'nyi': 'にぃ', 'nyu': 'にゅ', 'nye': 'にぇ', 'nyo': 'にょ', 'ha': 'は',
    'hi': 'ひ', 'hu': 'ふ', 'he': 'へ', 'ho': 'ほ', 'hya': 'ひゃ', 'hyi': 'ひぃ', 'hyu': 'ひゅ',
    'hye': 'ひぇ', 'hyo': 'ひょ', 'fwa': 'ふぁ', 'fwi': 'ふぃ', 'fwu': 'ふぅ', 'fwe': 'ふぇ',
    'fwo': 'ふぉ', 'fya': 'ふゃ', 'fyu': 'ふゅ', 'fyo': 'ふょ', 'ba': 'ば', 'bi': 'び',
    'bu': 'ぶ', 'be': 'べ', 'bo': 'ぼ', 'bya': 'びゃ', 'byi': 'びぃ', 'byu': 'びゅ', 'bye': 'びぇ',
    'byo': 'びょ', 'va': 'ゔぁ', 'vi': 'ゔぃ', 'vu': 'ゔ', 've': 'ゔぇ', 'vo': 'ゔぉ',
    'vya': 'ゔゃ', 'vyu': 'ゔゅ', 'vyo': 'ゔょ', 'pa': 'ぱ', 'pi': 'ぴ', 'pu': 'ぷ', 'pe': 'ぺ',
    'po': 'ぽ', 'pya': 'ぴゃ', 'pyi': 'ぴぃ', 'pyu': 'ぴゅ', 'pye': 'ぴぇ', 'pyo': 'ぴょ',
    'ma': 'ま', 'mi': 'み', 'mu': 'む', 'me': 'め', 'mo': 'も', 'mya': 'みゃ', 'myi': 'みぃ',
    'myu': 'みゅ', 'mye': 'みぇ', 'myo': 'みょ', 'ya': 'や', 'yu': 'ゆ', 'yo': 'よ',
    'xya': 'ゃ', 'xyu': 'ゅ', 'xyo': 'ょ', 'ra': 'ら', 'ri': 'り', 'ru': 'る', 're': 'れ',
    'ro': 'ろ', 'rya': 'りゃ', 'ryi': 'りぃ', 'ryu': 'りゅ', 'rye': 'りぇ', 'ryo': 'りょ',
    'wa': 'わ', 'wo': 'を', 'nn': 'ん', 'xwa': 'ゎ',
    '-': 'ー',
    'A': 'あ', 'I': 'い', 'U': 'う', 'E': 'え', 'O': 'お', 'YE': 'いぇ', 'WHA': 'うぁ',
    'WHI': 'うぃ', 'WHE': 'うぇ', 'WHO': 'うぉ', 'WYI': 'ゐ', 'WYE': 'ゑ', 'XA': 'ぁ',
    'XI': 'ぃ', 'XU': 'ぅ', 'XE': 'ぇ', 'XO': 'ぉ', 'KA': 'か', 'KI': 'き', 'KU': 'く',
    'KE': 'け', 'KO': 'こ', 'KYA': 'きゃ', 'KYI': 'きぃ', 'KYU': 'きゅ', 'KYE': 'きぇ',
    'KYO': 'きょ', 'QYA': 'くゃ', 'QYU': 'くゅ', 'QYO': 'くょ', 'QWA': 'くぁ', 'QWI': 'くぃ',
    'QWU': 'くぅ', 'QWE': 'くぇ', 'QWO': 'くぉ', 'GA': 'が', 'GI': 'ぎ', 'GU': 'ぐ',
    'GE': 'げ', 'GO': 'ご', 'GYA': 'ぎゃ', 'GYI': 'ぎぃ', 'GYU': 'ぎゅ', 'GYE': 'ぎぇ',
    'GYO': 'ぎょ', 'GWA': 'ぐぁ', 'GWI': 'ぐぃ', 'GWU': 'ぐぅ', 'GWE': 'ぐぇ', 'GWO': 'ぐぉ',
    'XKA': 'ゕ', 'XKE': 'ゖ', 'SA': 'さ', 'SI': 'し', 'SU': 'す', 'SE': 'せ', 'SO': 'そ',
    'SYA': 'しゃ', 'SYI': 'しぃ', 'SYU': 'しゅ', 'SYE': 'しぇ', 'SYO': 'しょ', 'SWA': 'すぁ',
    'SWI': 'すぃ', 'SWU': 'すぅ', 'SWE': 'すぇ', 'SWO': 'すぉ', 'ZA': 'ざ', 'ZI': 'じ',
    'ZU': 'ず', 'ZE': 'ぜ', 'ZO': 'ぞ', 'ZYA': 'じゃ', 'ZYI': 'じぃ', 'ZYU': 'じゅ', 'ZYE': 'じぇ',
    'ZYO': 'じょ', 'TA': 'た', 'TI': 'ち', 'TU': 'つ', 'TE': 'て', 'TO': 'と', 'TYA': 'ちゃ',
    'TYI': 'ちぃ', 'TYU': 'ちゅ', 'TYE': 'ちぇ', 'TYO': 'ちょ', 'TSA': 'つぁ', 'TSI': 'つぃ',
    'TSE': 'つぇ', 'TSO': 'つぉ', 'THA': 'てゃ', 'THI': 'てぃ', 'THU': 'てゅ', 'THE': 'てぇ',
    'THO': 'てょ', 'TWA': 'とぁ', 'TWI': 'とぃ', 'TWU': 'とぅ', 'TWE': 'とぇ', 'TWO': 'とぉ',
    'DA': 'だ', 'DI': 'ぢ', 'DU': 'づ', 'DE': 'で', 'DO': 'ど', 'DYA': 'ぢゃ', 'DYI': 'ぢぃ',
    'DYU': 'ぢゅ', 'DYE': 'ぢぇ', 'DYO': 'ぢょ', 'DHA': 'でゃ', 'DHI': 'でぃ', 'DHU': 'でゅ',
    'DHE': 'でぇ', 'DHO': 'でょ', 'DWA': 'どぁ', 'DWI': 'どぃ', 'DWU': 'どぅ', 'DWE': 'どぇ',
    'DWO': 'どぉ', 'XTU': 'っ', 'NA': 'な', 'NI': 'に', 'NU': 'ぬ', 'NE': 'ね', 'NO': 'の',
    'NYA': 'にゃ', 'NYI': 'にぃ', 'NYU': 'にゅ', 'NYE': 'にぇ', 'NYO': 'にょ', 'HA': 'は',
    'HI': 'ひ', 'HU': 'ふ', 'HE': 'へ', 'HO': 'ほ', 'HYA': 'ひゃ', 'HYI': 'ひぃ', 'HYU': 'ひゅ',
    'HYE': 'ひぇ', 'HYO': 'ひょ', 'FWA': 'ふぁ', 'FWI': 'ふぃ', 'FWU': 'ふぅ', 'FWE': 'ふぇ',
    'FWO': 'ふぉ', 'FYA': 'ふゃ', 'FYU': 'ふゅ', 'FYO': 'ふょ', 'BA': 'ば', 'BI': 'び',
    'BU': 'ぶ', 'BE': 'べ', 'BO': 'ぼ', 'BYA': 'びゃ', 'BYI': 'びぃ', 'BYU': 'びゅ', 'BYE': 'びぇ',
    'BYO': 'びょ', 'VA': 'ゔぁ', 'VI': 'ゔぃ', 'VU': 'ゔ', 'VE': 'ゔぇ', 'VO': 'ゔぉ',
    'VYA': 'ゔゃ', 'VYU': 'ゔゅ', 'VYO': 'ゔょ', 'PA': 'ぱ', 'PI': 'ぴ', 'PU': 'ぷ', 'PE': 'ぺ',
    'PO': 'ぽ', 'PYA': 'ぴゃ', 'PYI': 'ぴぃ', 'PYU': 'ぴゅ', 'PYE': 'ぴぇ', 'PYO': 'ぴょ',
    'MA': 'ま', 'MI': 'み', 'MU': 'む', 'ME': 'め', 'MO': 'も', 'MYA': 'みゃ', 'MYI': 'みぃ',
    'MYU': 'みゅ', 'MYE': 'みぇ', 'MYO': 'みょ', 'YA': 'や', 'YU': 'ゆ', 'YO': 'よ',
    'XYA': 'ゃ', 'XYU': 'ゅ', 'XYO': 'ょ', 'RA': 'ら', 'RI': 'り', 'RU': 'る', 'RE': 'れ',
    'RO': 'ろ', 'RYA': 'りゃ', 'RYI': 'りぃ', 'RYU': 'りゅ', 'RYE': 'りぇ', 'RYO': 'りょ',
    'WA': 'わ', 'WO': 'を', 'NN': 'ん', 'XWA': 'ゎ'
}

def convert_romaji_to_kana(romaji_text):
    # 排序以便更長的羅馬字能夠首先被替換
    sorted_romaji_to_kana = sorted(romaji_to_kana.items(), key=lambda x: -len(x[0]))
    for romaji, kana in sorted_romaji_to_kana:
        romaji_text = romaji_text.replace(romaji, kana)
    return romaji_text

def process_text_file(input_file, output_file):
    seen_lines = set()  # 去重
    processing = False
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        lines_to_write = []
        for line in infile:
            if not processing:
                lines_to_write.append(line)
                if line.strip() == '...':
                    processing = True
            else:
                columns = line.strip().split('\t')
                if len(columns) > 1:
                    columns[1] = convert_romaji_to_kana(columns[1].replace(" ", ""))
                processed_line = '\t'.join(columns)
                # 去重
                if processed_line not in seen_lines:
                    lines_to_write.append(processed_line + '\n')
                    seen_lines.add(processed_line)
                if 'jaroomaji' in line:
                    line = line.replace('jaroomaji', 'kikwin')
        
        lines_to_write.insert(3, "# 此詞庫從rime-jaroomaji自動轉換\n")
        lines_to_write.insert(4, "# RIME版底本: https://github.com/lazyfoxchan/rime-jaroomaji\n")
        lines_to_write.insert(5, "#\n")
        lines_to_write.insert(6, "# 此爲菊韻和語輸入法字表詞庫文件\n")
        lines_to_write.insert(7, "# 瞭解如何使用菊韻請閱覽readme文件，詳細請至本方案github頁：\n")
        lines_to_write.insert(8, "# https://github.com/HoengSaan/rime-kikwin\n")
        lines_to_write.insert(9, "# This is a dictionary file for Kikwin Japanese Input Method.\n")
        lines_to_write.insert(10, "# Learn how to use Kikwin in the readme file, available on the project's github page.\n")
        lines_to_write.insert(11, "#\n")
        
        outfile.writelines(lines_to_write)

# 自動轉換
input1 = 'jaroomaji.jmdict.dict.yaml'
input2 = 'jaroomaji.kanjidic2.dict.yaml'
input3 = 'jaroomaji.mozc.dict.yaml'
input4 = 'jaroomaji.mozcemoji.dict.yaml'
output1 = 'kikwin.jmdict.dict.yaml'
output2 = 'kikwin.kanjidic2.dict.yaml'
output3 = 'kikwin.mozc.dict.yaml'
output4 = 'kikwin.mozcemoji.dict.yaml'
print("start converting")
process_text_file(input1, output1)
print(input1, "converted")
process_text_file(input2, output2)
print(input2, "converted")
process_text_file(input3, output3)
print(input3, "converted")
process_text_file(input4, output4)
print(input4, "converted")
print("finish")
input("Press Enter to continue...")