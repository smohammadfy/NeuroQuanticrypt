# NeuroQuanticrypt 🔒🧠

An innovative hybrid encryption framework that combines the power of quantum-resistant cryptography, neural networks, and homomorphic encryption.

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-experimental-orange)
![Cryptography](https://img.shields.io/badge/crypto-advanced-brightgreen)

## 🌟 Key Features

- **🧠 Neural Network-Based Encryption** - Dynamic algorithm with block-to-block feedback
- **🛡️ Quantum-Resistant** - Post-quantum cryptography algorithms
- **🔐 Homomorphic Encryption** - Perform computations on encrypted data
- **🎯 Three-Layer Security** - Multi-layer architecture for maximum protection
- **⚡ Dynamic & Adaptive** - Neural models that adapt to data patterns
- **🔑 Zero-Trust Model** - End-to-end encryption with client-side key management

## 🏗️ Architecture Overview

NeuroQuanticrypt employs a sophisticated three-layer security model:

### Layer 1: Neural Dynamic Encryption (NDE)
- Custom neural network for keystream generation
- Block-to-block feedback mechanism
- Data-dependent encryption patterns

### Layer 2: Post-Quantum Cryptography (PQC)
- Quantum-resistant key encapsulation
- HKDF-based key derivation
- Future-proof security

### Layer 3: Homomorphic Encryption (HE)
- Secure computations on encrypted data
- Support for arithmetic operations
- Cloud processing capabilities

# Clone the repository
git clone https://github.com/smohammadfy/neuroquanticrypt.git
cd neuroquanticrypt

# Install dependencies
pip install torch cryptography numpy

# details:
Project: Design and Implementation of a Hybrid Quantum-Resistant Cryptography Framework Using Neural Networks and Homomorphic Cryptography
Project Name: NeuroQuanticrypt
1. The main goal of the project
To create a cryptographic framework that:
1. Is resistant to quantum computers (Post-Quantum Cryptography).
2. Uses machine learning to create dynamic cryptographic models based on data patterns.
3. Provides the ability to compute on encrypted data (Fully Homomorphic Encryption - FHE) for cloud applications.
4. Follows a Zero-Trust model, so that even the service provider cannot access the raw data.
The project creates three independent but integrated security layers.
2. Main Components
a) Layer 1: Neural-Based Dynamic Encryption (NDE)
• Innovation: Instead of using fixed mathematical functions like AES or RSA, a neural network is used to generate the keystream. The network generates a unique encryption pattern based on the input data (Plaintext) itself and a master key.
• Mechanism:
1. Preparation: The data is divided into n-byte blocks.
2. Keystream generation: A lightweight neural network such as a small convolutional network or LSTM receives each block and generates a complex random byte sequence (Keystream). The weights of this network are initialized using the master key and a Salt.
3. Encryption: A simple XOR operation is performed between the data block and the generated keystream.
4. Dynamic: After encrypting each block, the output of the neural network is injected into the input of the next block based on a feedback function. This makes the encryption pattern for each block dependent on the previous block and is highly resistant to pattern analysis.
b) Second layer: Post-Quantum Layer (PQL)
• Innovation: Using a standard and approved CRYSTALS-Kyber algorithm for key exchange or for signing as an independent but integrated layer.
• Mechanism:
1. The master key used in the NDE layer is itself encrypted with the Kyber algorithm.
2. This encrypted key is then stored in the encrypted file header.
3. For decryption, the master key must first be recovered using the Kyber private key. This ensures the security of the system even in the event of a failure of the neural layer.
c) Layer 3: Selective Homomorphic Encryption (SHE)
• Innovation: This layer allows performing specific calculations (such as addition or multiplication) on the encrypted data of the NDE layer, without requiring full decryption.
• Mechanism:
1. A lightweight homomorphic encryption scheme is used.
2. This layer is optionally enabled only for specific data fields that require cloud processing (e.g. "age" or "transaction amount").
3. The data for these fields is encrypted once again with FHE and stored along with the original encrypted data.

3. Key Benefits and Innovations
1. Three-layer security: Breaking one layer does not mean accessing the data.
2. Quantum resistance: The core of the system is based on quantum-resistant cryptography.
3. Dynamics and Adaptability: The Neural Engine (NDE) layer changes the encryption pattern based on the data, which makes it very difficult to analyze the code.
4. Secure Cloud Computing Capability: The FHE layer allows the use of cloud computing power without compromising privacy.
5. Zero Trust Model: The master key is only with the end user. Data in the cloud is fully encrypted and unreadable.

4. Potential Applications
• Data Security in Cloud Computing: For companies that store sensitive data in the cloud but need to query and analyze it.
• Health Data Protection: Ability to share patient data between research centers without revealing personal information.
• Security in Financial and Banking Systems: To protect transactions and customer information against future threats (quantum).
• Military and Government Systems: To keep information confidential at the highest level.

پروژه: طراحی و پیاده‌سازی چارچوب رمزنگاری کوانتومی-مقاوم هیبریدی با استفاده از شبکه‌های عصبی و رمزنگاری همومورفیک
نام پروژه: NeuroQuanticrypt  
1.	هدف اصلی پروژه
ایجاد یک چارچوب رمزنگاری که:
1.	مقاوم در برابر کامپیوترهای کوانتومی باشد (Post-Quantum Cryptography).
2.	از یادگیری ماشین برای ایجاد مدل‌های رمزنگاری پویا و مبتنی بر الگوی داده‌ها استفاده کند.
3.	قابلیت محاسبه روی داده‌های رمز شده (Fully Homomorphic Encryption - FHE) را برای کاربردهای ابری فراهم کند.
4.	از یک مدل اعتماد صفر (Zero-Trust) پیروی کند، به طوری که حتی ارائه‌دهنده سرویس نیز نتواند به داده‌های خام دسترسی داشته باشد.
این پروژه سه لایه امنیتی مستقل اما یکپارچه ایجاد می‌کند.
2.	 اجزای اصلی 
الف) لایه اول: رمزنگاری مبتنی بر شبکه عصبی (Neural-Based Dynamic Encryption - NDE)
•	نوآوری: به جای استفاده از توابع ثابت ریاضی مانند AES یا RSA، از یک شبکه عصبی برای تولید جریان کلید (Keystream) استفاده می‌شود. این شبکه بر اساس خود داده‌ی ورودی (Plaintext) و یک کلید اصلی (Master Key)، یک الگوی رمزنگاری منحصربه‌فرد تولید می‌کند.
•	مکانیزم:
1.	آماده‌سازی: داده به بلوک‌های n-بایتی تقسیم می‌شود.
2.	تولید جریان کلید: یک شبکه عصبی سبک‌وزن مانند یک شبکه کانولوشنی کوچک یا LSTM هر بلوک را دریافت کرده و یک دنباله بایت تصادفی پیچیده (Keystream) تولید می‌کند. وزن‌های این شبکه با استفاده از کلید اصلی و یک Salt مقداردهی اولیه می‌شوند.
3.	رمزنگاری: یک عملگر XOR ساده بین بلوک داده و جریان کلید تولیدشده انجام می‌شود.
4.	پویایی (Dynamic): پس از رمز کردن هر بلوک، خروجی شبکه عصبی بر اساس یک تابع بازخورد، به ورودی بلوک بعدی تزریق می‌شود. این کار الگوی رمزنگاری را برای هر بلوک وابسته به بلوک قبلی می‌کند و در برابر تحلیل الگو بسیار مقاوم است.
ب) لایه دوم: رمزنگاری کوانتومی-مقاوم (Post-Quantum Layer - PQL)
•	نوآوری: استفاده از یک الگوریتم استاندارد و مورد تایید CRYSTALS-Kyber برای تبادل کلید یا  برای امضا به عنوان یک لایه مستقل اما یکپارچه.
•	مکانیزم:
1.	کلید اصلی (Master Key) مورد استفاده در لایه NDE، خود با الگوریتم Kyber رمزگذاری می‌شود.
2.	این کلید رمز شده سپس در هدر فایل رمزگذاری شده ذخیره می‌گردد.
3.	برای رمزگشایی، ابتدا باید کلید اصلی با استفاده از کلید خصوصی Kyber بازیابی شود. این کار امنیت سیستم را حتی در صورت شکست لایه عصبی نیز تضمین می‌کند.
ج) لایه سوم: رمزنگاری همومورفیک انتخابی (Selective Homomorphic Encryption - SHE)
•	نوآوری: این لایه امکان انجام محاسبات خاص (مانند جمع یا ضرب) را روی داده‌های رمز شده لایه NDE فراهم می‌کند، بدون نیاز به رمزگشایی کامل.
•	مکانیزم:
1.	از یک طرح رمزنگاری همومورفیک سبک‌وزن استفاده می‌شود.
2.	این لایه به صورت اختیاری و فقط برای فیلدهای دادهای خاص که نیاز به پردازش ابری دارند (مثلاً "سن" یا "مبلغ تراکنش") فعال می‌شود.
3.	داده‌های مربوط به این فیلدها یک بار دیگر با FHE رمز می‌شوند و به همراه داده‌های رمز شده اصلی ذخیره می‌گردند.
 
3. 	 مزایای کلیدی و نوآوری‌ها
1.	امنیت سه لایه: شکستن یک لایه به معنای دستیابی به داده‌ها نیست.
2.	مقاومت در برابر کوانتوم: هسته اصلی سیستم بر پایه رمزنگاری کوانتومی-مقاوم است.
3.	پویایی و تطبیق‌پذیری: لایه عصبی (NDE) الگوی رمزنگاری را بر اساس داده‌ها تغییر می‌دهد، که تحلیل رمز را بسیار سخت می‌کند.
4.	قابلیت پردازش ابری امن: لایه FHE امکان استفاده از قدرت پردازشی ابر بدون به خطر افتادن حریم خصوصی را فراهم می‌کند.
5.	مدل اعتماد صفر: کلید اصلی فقط نزد کاربر نهایی است. داده‌های موجود در ابر به طور کامل رمز شده و غیرقابل خواندن هستند.

4.	کاربردهای بالقوه
•	امنیت داده در رایانش ابری: برای شرکت‌هایی که داده‌های حساس را در ابر ذخیره می‌کنند اما نیاز به انجام Query و تحلیل روی آن‌ها دارند.
•	حفاظت از داده‌های پزشکی (Health Data): امکان اشتراک‌گذاری داده‌های بیماران بین مراکز تحقیقاتی بدون افشای اطلاعات شخصی.
•	امنیت در سیستم‌های مالی و بانکی: برای محافظت از تراکنش‌ها و اطلاعات مشتریان در برابر تهدیدات آینده (کوانتومی).
•	سیستم‌های نظامی و دولتی: برای محرمانه نگه داشتن اطلاعات در بالاترین سطح.

