class EnigmaMachine:
    def __init__(self, rotor_positions=None):
        if rotor_positions is None:
            rotor_positions = [1, 1, 1]
        self.rotor_positions = rotor_positions
        self.reflector = [3, 15, 6, 24, 8, 17, 20, 7, 16, 5, 18, 11, 10, 23, 2, 25, 14, 22, 13, 9, 12, 21, 19, 4, 1, 0]
        self.rotors = [
            [18, 24, 22, 6, 12, 3, 16, 20, 8, 15, 23, 13, 1, 2, 25, 9, 17, 0, 5, 14, 7, 11, 10, 19, 21, 4],
            [0, 9, 3, 10, 18, 8, 17, 20, 23, 1, 11, 13, 22, 24, 12, 7, 25, 5, 16, 6, 4, 21, 14, 15, 2, 19],
            [14, 12, 16, 6, 4, 7, 0, 23, 18, 10, 1, 22, 25, 5, 15, 11, 24, 17, 13, 20, 2, 8, 19, 21, 9, 3]
        ]

    def encrypt(self, letter):
        letter_idx = ord(letter) - ord('A')
        for i in range(3):
            letter_idx = (letter_idx + self.rotor_positions[i]) % 26
            letter_idx = self.rotors[i][letter_idx]
            letter_idx = (letter_idx - self.rotor_positions[i] + 26) % 26
        letter_idx = self.reflector[letter_idx]
        for i in range(2, -1, -1):
            letter_idx = (letter_idx + self.rotor_positions[i]) % 26
            letter_idx = self.rotors[i][letter_idx]
            letter_idx = (letter_idx - self.rotor_positions[i] + 26) % 26

        encrypted_letter = chr(letter_idx + ord('A'))
        self.rotate_rotors()  # Rotation des rotors uniquement lors du cryptage
        return encrypted_letter

    def decrypt(self, letter):
        letter_idx = ord(letter) - ord('A')
        for i in range(2, -1, -1):
            letter_idx = (letter_idx + self.rotor_positions[i]) % 26
            letter_idx = self.rotors[i].index(letter_idx)
            letter_idx = (letter_idx - self.rotor_positions[i] + 26) % 26
        letter_idx = self.reflector[letter_idx]
        for i in range(2):  # Modification ici pour ne pas effectuer la rotation du rotor 3 lors du décryptage
            letter_idx = (letter_idx + self.rotor_positions[i]) % 26
            letter_idx = self.rotors[i][letter_idx]
            letter_idx = (letter_idx - self.rotor_positions[i] + 26) % 26

        decrypted_letter = chr(letter_idx + ord('A'))
        return decrypted_letter

    def rotate_rotors(self):
        self.rotor_positions[0] = (self.rotor_positions[0] + 1) % 26
        if self.rotor_positions[0] == 0:
            self.rotor_positions[1] = (self.rotor_positions[1] + 1) % 26
            if self.rotor_positions[1] == 0:
                self.rotor_positions[2] = (self.rotor_positions[2] + 1) % 26

def launch_machine():
    # Permet à l'utilisateur de choisir la position initiale des rotors
    user_rotor_positions = [int(input(f"Position initiale du rotor {i + 1}: ")) for i in range(3)]

    # Crée une instance de la machine Enigma avec les positions choisies par l'utilisateur
    enigma = EnigmaMachine(rotor_positions=user_rotor_positions)

    # Demande à l'utilisateur d'entrer le message à crypter
    message = input("Message à crypter: ")

    # Demande à l'utilisateur s'il veut crypter ou décrypter
    choice = input("Voulez-vous crypter (C) ou décrypter (D) ? ").upper()

    # Traite le choix de l'utilisateur
    if choice == 'C':
        result = ''.join(enigma.encrypt(letter) for letter in message)
        print(f"Message crypté: {result}")
    elif choice == 'D':
        result = ''.join(enigma.decrypt(letter) for letter in message)
        print(f"Message décrypté: {result}")
    else:
        print("Choix invalide. Veuillez choisir 'C' pour crypter ou 'D' pour décrypter.")
