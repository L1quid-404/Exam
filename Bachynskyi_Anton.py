# .bachynskyi_exam
import sys
from googletrans import Translator

lang = "Japanese"

BLUE = "\033[34m"
RED = "\033[31m"
RESET = "\033[0m"

translator = Translator()

def translate_msg(text, target_lang):
    try:
        return translator.translate(text, src='uk', dest=target_lang).text
    except Exception:
        return text

def main():
    prompt_txt = "Введіть довжини сторін трикутника a, b, c: "
    exists_txt = "Трикутник з сторонами {} існує."
    iso_txt = " є рівнобедреним"
    reason_txt = " так як дві його сторони дорівнюють "

    p_label = translate_msg(prompt_txt, lang)
    
    user_input = input(p_label)
    try:
        sides = [float(x) for x in user_input.split()]
        if len(sides) != 3: raise ValueError
        a, b, c = sides
    except ValueError:
        print("Error: Input 3 numbers.")
        return

    def f(n): return str(int(n) if n.is_integer() else n)

    if (a + b > c) and (a + c > b) and (b + c > a):
        translated_exists = translate_msg(exists_txt, lang)
        sides_blue = f"{BLUE}{f(a)},{f(b)},{f(c)}{RESET}"
        print(translated_exists.format(sides_blue))

        iso_data = None
        if a == b: iso_data = a
        elif a == c: iso_data = a
        elif b == c: iso_data = b

        if iso_data:
            res_iso = translate_msg(iso_txt, lang)
            res_reason = translate_msg(reason_txt, lang)
            
            sides_red = f"{RED}{f(a)}, {f(b)}, {f(c)}{RESET}"
            print(f"Triangle {sides_red}{BLUE}{res_iso}{RESET}{res_reason}{RED}{f(iso_data)}{RESET}.")
    else:
        print(translate_msg("Трикутник не існує.", lang))

if __name__ == "__main__":
    main()