#Project 3: Guess the Number Game Python Project (user)
def user_based_guess_game():
    """صارف بیسڈ نمبر گیس گیم: ایک صارف نمبر داخل کرتا ہے، دوسرا اندازہ لگاتا ہے۔"""
    
    # پہلے صارف سے خفیہ نمبر کی ان پٹ
    while True:
        try:
            secret_number = int(input("\nپہلے صارف: براہ کرم 1 سے 100 کے درمیان ایک نمبر داخل کریں: "))
            if 1 <= secret_number <= 100:
                break
            else:
                print("نمبر 1 سے 100 کے درمیان ہونا چاہیے۔")
        except ValueError:
            print("غلط ان پٹ! صرف عددی نمبر داخل کریں۔")

    # اسکرین کلئیر کرنے کے لیے (صارف کو خفیہ نمبر نہ دکھائی دے)
    print("\n" * 50)

    # دوسرے صارف سے اندازہ لگوانا
    guesses_left = 7
    print("\nدوسرے صارف: اندازہ لگائیں کہ خفیہ نمبر کیا ہے!")
    
    while guesses_left > 0:
        print(f"\nآپ کے پاس {guesses_left} کوششیں باقی ہیں۔")
        try:
            guess = int(input("اندازہ لگائیں: "))
        except ValueError:
            print("غلط ان پٹ! صرف عددی نمبر داخل کریں۔")
            continue

        if guess < secret_number:
            print("بہت چھوٹا! دوبارہ کوشش کریں۔")
        elif guess > secret_number:
            print("بہت بڑا! دوبارہ کوشش کریں۔")
        else:
            print(f"مبارک ہو! آپ نے صرف {7 - guesses_left + 1} کوششوں میں نمبر تلاش کر لیا!")
            return

        guesses_left -= 1

    print(f"\nکوششیں ختم ہو گئیں! خفیہ نمبر تھا: {secret_number}")

user_based_guess_game()