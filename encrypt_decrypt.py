while True:
    print('Choose an option: \n\t 1)Encrypt \n\t 2)Decrypt \n\t 3)Exit')
    Entry = input("Enter a number:")
    
    if Entry == '1':
        print('Enter your text which must be ENCRYPTED:')
        txt_in = input('Enter:')
        print('Encrypting....')
        encrypted_txt = ''
        for i in txt_in:
            a = ord(i) * 24 - 12 + 72
            encrypted_txt += chr(a)
        print(f'Encrypted text: {encrypted_txt}')
        print('\n <<---------------------------------------------------------->> ')
        
    elif Entry == '2':
        print('Enter your text which must be DECRYPTED:')
        txt_out = input('Enter:')
        print('DEcrypting....')
        decrypte_txt = ''
        for i in txt_out:
            a = ((ord(i) - 72) + 12 ) // 24
            decrypte_txt += chr(a)
        print(f'Decrypted text: {decrypte_txt}')
        print('\n <<---------------------------------------------------------->> ')

    elif Entry == '3':
        print('Take Care.')
        break
    else:
        print("Incorrect Entry!")