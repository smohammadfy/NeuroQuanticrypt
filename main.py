import numpy as np
import torch
import torch.nn as nn
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os
import struct


# ==================== لایه 1: شبکه عصبی برای رمزنگاری (NDE) ====================

class NeuralCryptoNet(nn.Module):
    def __init__(self, input_size=32, hidden_size=64, output_size=32):
        super(NeuralCryptoNet, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, hidden_size)
        self.fc3 = nn.Linear(hidden_size, output_size)
        self.activation = nn.Tanh()

    def forward(self, x, feedback=None):
        if feedback is not None:
            x = torch.cat([x, feedback], dim=-1)
            if x.shape[1] > 32:
                x = nn.Linear(x.shape[1], 32)(x)

        x = self.activation(self.fc1(x))
        x = self.activation(self.fc2(x))
        x = torch.sigmoid(self.fc3(x))
        return x


class NeuralDynamicEncryption:
    def __init__(self, master_key):
        self.model = NeuralCryptoNet()
        self.master_key = master_key
        self._initialize_weights()

    def _initialize_weights(self):
        """مقداردهی وزن‌ها بر اساس کلید اصلی"""
        seed = int.from_bytes(self.master_key[:8], byteorder='big')
        torch.manual_seed(seed)

        for param in self.model.parameters():
            param.data.uniform_(-1, 1)

    def generate_keystream(self, data_block, previous_output=None):
        """تولید جریان کلید با شبکه عصبی"""
        with torch.no_grad():
            if len(data_block) < 32:
                data_block = data_block + b'\x00' * (32 - len(data_block))

            input_data = [float(byte) / 255.0 for byte in data_block[:32]]
            input_tensor = torch.tensor(input_data, dtype=torch.float32).unsqueeze(0)

            feedback_tensor = None
            if previous_output is not None:
                feedback_data = [float(byte) / 255.0 for byte in previous_output[:16]]
                if len(feedback_data) < 16:
                    feedback_data += [0.0] * (16 - len(feedback_data))
                feedback_tensor = torch.tensor(feedback_data, dtype=torch.float32).unsqueeze(0)

            output = self.model(input_tensor, feedback_tensor)
            keystream = bytes([int(x * 255) for x in output.squeeze().tolist()])
            return keystream[:len(data_block)]

    def encrypt_block(self, data_block, previous_output=None):
        """رمزنگاری یک بلوک داده"""
        keystream = self.generate_keystream(data_block, previous_output)
        encrypted = bytes(a ^ b for a, b in zip(data_block, keystream))
        return encrypted, keystream

    def decrypt_block(self, encrypted_block, previous_output=None):
        """رمزگشایی یک بلوک داده"""
        return self.encrypt_block(encrypted_block, previous_output)[0]


# ==================== لایه 2: رمزنگاری کوانتومی-مقاوم  ====================

class PostQuantumCrypto:
    """شبیه‌سازی رمزنگاری کوانتومی-مقاوم"""

    @staticmethod
    def encrypt_key(master_key, public_key=None):
        """رمزنگاری کلید اصلی"""
        salt = os.urandom(32)
        kdf = HKDF(
            algorithm=hashes.SHA256(),
            length=len(master_key),
            salt=salt,
            info=b'pqc_encryption',
        )
        encrypted_key = kdf.derive(master_key)
        return encrypted_key, salt

    @staticmethod
    def decrypt_key(encrypted_key, private_key, salt):
        """رمزگشایی کلید اصلی"""
        kdf = HKDF(
            algorithm=hashes.SHA256(),
            length=len(encrypted_key),
            salt=salt,
            info=b'pqc_encryption',
        )
        try:
            master_key = kdf.derive(encrypted_key)
            return master_key
        except:
            return private_key


# ==================== لایه 3: رمزنگاری همومورفیک  ====================

class HomomorphicEncryption:
    """شبیه‌سازی رمزنگاری همومورفیک برای اعداد"""

    @staticmethod
    def encrypt_number(number, key):
        """رمزنگاری همومورفیک ساده"""
        noise = int.from_bytes(key[:4], byteorder='big') % 1000
        encrypted = (number * 1000) + noise
        return encrypted.to_bytes(8, byteorder='big')

    @staticmethod
    def decrypt_number(encrypted_data, key):
        """رمزگشایی همومورفیک"""
        encrypted_num = int.from_bytes(encrypted_data, byteorder='big')
        noise = int.from_bytes(key[:4], byteorder='big') % 1000
        number = (encrypted_num - noise) // 1000
        return number

    @staticmethod
    def homomorphic_add(encrypted_a, encrypted_b):
        """جمع همومورفیک"""
        a_num = int.from_bytes(encrypted_a, byteorder='big')
        b_num = int.from_bytes(encrypted_b, byteorder='big')
        result = a_num + b_num
        return result.to_bytes(8, byteorder='big')

    @staticmethod
    def homomorphic_multiply(encrypted_a, scalar):
        """ضرب همومورفیک در اسکالر"""
        a_num = int.from_bytes(encrypted_a, byteorder='big')
        result = a_num * scalar
        return result.to_bytes(8, byteorder='big')


# ==================== چارچوب اصلی NeuroQuanticrypt ====================

class NeuroQuanticrypt:
    def __init__(self, master_key=None):
        if master_key is None:
            master_key = os.urandom(32)
        self.master_key = master_key
        self.neural_crypto = NeuralDynamicEncryption(master_key)

    def encrypt(self, data, fields_to_encrypt_homomorphically=None):
        """رمزنگاری داده با چارچوب کامل"""
        encrypted_master_key, salt = PostQuantumCrypto.encrypt_key(self.master_key)

        block_size = 32
        encrypted_blocks = []
        previous_output = None

        for i in range(0, len(data), block_size):
            block = data[i:i + block_size]
            encrypted_block, keystream = self.neural_crypto.encrypt_block(block, previous_output)
            encrypted_blocks.append(encrypted_block)
            previous_output = keystream

        main_encrypted_data = b''.join(encrypted_blocks)

        homomorphic_data = {}
        if fields_to_encrypt_homomorphically:
            for field_name, value in fields_to_encrypt_homomorphically.items():
                if isinstance(value, int):
                    encrypted_value = HomomorphicEncryption.encrypt_number(value, self.master_key)
                    homomorphic_data[field_name] = encrypted_value

        header = {
            'encrypted_master_key': encrypted_master_key,
            'salt': salt,
            'data_size': len(data),
            'block_size': block_size,
            'homomorphic_fields': list(homomorphic_data.keys()) if homomorphic_data else []
        }

        return {
            'header': header,
            'encrypted_data': main_encrypted_data,
            'homomorphic_data': homomorphic_data
        }

    def decrypt(self, encrypted_package, private_key=None):
        """رمزگشایی داده"""
        header = encrypted_package['header']
        encrypted_data = encrypted_package['encrypted_data']

        master_key = PostQuantumCrypto.decrypt_key(
            header['encrypted_master_key'],
            private_key or self.master_key,
            header['salt']
        )

        self.neural_crypto = NeuralDynamicEncryption(master_key)

        block_size = header['block_size']
        decrypted_blocks = []
        previous_output = None

        for i in range(0, len(encrypted_data), block_size):
            block = encrypted_data[i:i + block_size]
            decrypted_block = self.neural_crypto.decrypt_block(block, previous_output)
            decrypted_blocks.append(decrypted_block)
            previous_output = block[:16] if len(block) >= 16 else block

        decrypted_data = b''.join(decrypted_blocks)[:header['data_size']]
        return decrypted_data


# ==================== توابع کمکی ====================

def bytes_to_hex_string(data, max_length=50):
    """تبدیل بایت‌ها به رشته hex برای نمایش امن"""
    hex_str = data.hex()
    if len(hex_str) > max_length:
        return hex_str[:max_length] + "..."
    return hex_str


def safe_decode(data):
    """تبدیل امن بایت‌ها به رشته"""
    try:
        return data.decode('utf-8')
    except UnicodeDecodeError:
        # اگر UTF-8 معتبر نیست، از repr استفاده کن
        return repr(data)


# ==================== تست و نمایش عملکرد ====================

def test_neuroquanticrypt():
    print("=== Testing NeuroQuanticrypt System ===\n")

    crypto_system = NeuroQuanticrypt()

    # تست با داده‌های مختلف
    test_cases = [
        b"Simple text message",
        b"Confidential data: 12345",
        b"X" * 50,  # داده تکراری
        os.urandom(64)  # داده تصادفی
    ]

    homomorphic_fields = {
        'age': 25,
        'salary': 5000,
        'score': 85
    }

    for i, sample_data in enumerate(test_cases):
        print(f"\n--- Test Case {i + 1} ---")
        print(f"Original data ({len(sample_data)} bytes): {safe_decode(sample_data)}")
        print(f"Original data (hex): {bytes_to_hex_string(sample_data)}")

        # رمزنگاری
        encrypted_package = crypto_system.encrypt(sample_data, homomorphic_fields)

        print(f"Encrypted data (hex): {bytes_to_hex_string(encrypted_package['encrypted_data'])}")

        # رمزگشایی
        decrypted_data = crypto_system.decrypt(encrypted_package)

        print(f"Decrypted data ({len(decrypted_data)} bytes): {safe_decode(decrypted_data)}")
        print(f"Decrypted data (hex): {bytes_to_hex_string(decrypted_data)}")

        # اعتبارسنجی
        success = sample_data == decrypted_data
        print(f"Decryption successful: {success}")

        if not success:
            print("ERROR: Data corruption detected!")
            print(f"Original first 10 bytes: {sample_data[:10].hex()}")
            print(f"Decrypted first 10 bytes: {decrypted_data[:10].hex()}")

    print("\n" + "=" * 60)


def test_homomorphic_operations():
    print("\n=== Testing Homomorphic Operations ===")

    crypto_system = NeuroQuanticrypt()

    homomorphic_fields = {
        'age': 25,
        'salary': 5000,
        'score': 85
    }

    sample_data = b"Test data for homomorphic operations"
    encrypted_package = crypto_system.encrypt(sample_data, homomorphic_fields)

    # تست عملیات همومورفیک
    if 'age' in encrypted_package['homomorphic_data']:
        encrypted_age = encrypted_package['homomorphic_data']['age']
        encrypted_score = encrypted_package['homomorphic_data']['score']

        # جمع همومورفیک
        encrypted_sum = HomomorphicEncryption.homomorphic_add(encrypted_age, encrypted_score)
        decrypted_sum = HomomorphicEncryption.decrypt_number(encrypted_sum, crypto_system.master_key)

        print(f"Homomorphic addition: {homomorphic_fields['age']} + {homomorphic_fields['score']} = {decrypted_sum}")
        print(f"Expected result: {homomorphic_fields['age'] + homomorphic_fields['score']}")
        print(f"Addition correct: {decrypted_sum == homomorphic_fields['age'] + homomorphic_fields['score']}")

        # ضرب همومورفیک
        encrypted_mult = HomomorphicEncryption.homomorphic_multiply(encrypted_age, 3)
        decrypted_mult = HomomorphicEncryption.decrypt_number(encrypted_mult, crypto_system.master_key)

        print(f"Homomorphic multiplication: {homomorphic_fields['age']} * 3 = {decrypted_mult}")
        print(f"Expected result: {homomorphic_fields['age'] * 3}")
        print(f"Multiplication correct: {decrypted_mult == homomorphic_fields['age'] * 3}")


def performance_test():
    """تست عملکرد با داده‌های بزرگتر"""
    print("\n=== Performance Test ===")

    crypto_system = NeuroQuanticrypt()

    # تست با سایزهای مختلف
    sizes = [128, 512, 1024, 2048]  # bytes

    for size in sizes:
        print(f"\nTesting with {size} bytes:")
        test_data = os.urandom(size)

        import time

        # رمزنگاری
        start_time = time.time()
        encrypted = crypto_system.encrypt(test_data)
        encrypt_time = time.time() - start_time

        # رمزگشایی
        start_time = time.time()
        decrypted = crypto_system.decrypt(encrypted)
        decrypt_time = time.time() - start_time

        success = test_data == decrypted

        print(f"  Encryption time: {encrypt_time:.4f}s")
        print(f"  Decryption time: {decrypt_time:.4f}s")
        print(f"  Encryption speed: {size / encrypt_time / 1024:.2f} KB/s")
        print(f"  Success: {success}")


def consistency_test():
    """تست سازگاری و قابلیت اطمینان"""
    print("\n=== Consistency Test ===")

    # تست با کلید یکسان
    master_key = os.urandom(32)
    crypto_system1 = NeuroQuanticrypt(master_key)
    crypto_system2 = NeuroQuanticrypt(master_key)

    test_data = b"Consistency test data"

    # رمزنگاری با دو سیستم مختلف اما با کلید یکسان
    encrypted1 = crypto_system1.encrypt(test_data)
    encrypted2 = crypto_system2.encrypt(test_data)

    # باید بتوانند داده‌های یکدیگر را رمزگشایی کنند
    decrypted1_by_2 = crypto_system2.decrypt(encrypted1)
    decrypted2_by_1 = crypto_system1.decrypt(encrypted2)

    print(f"System 1 can decrypt System 2: {test_data == decrypted2_by_1}")
    print(f"System 2 can decrypt System 1: {test_data == decrypted1_by_2}")
    print(f"Both encryptions are identical: {encrypted1['encrypted_data'] == encrypted2['encrypted_data']}")


if __name__ == "__main__":
    test_neuroquanticrypt()
    test_homomorphic_operations()
    performance_test()
    consistency_test()

    print("\n" + "=" * 60)
    print("All tests completed!")