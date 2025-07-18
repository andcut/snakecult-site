#!/usr/bin/env python3
"""
Translate Tag Matrix Script
Uses existing translations from data/tag_translations.json and adds machine translations for missing tags.
"""

import json
import os

# Configuration
ENGLISH_TAGS_FILE = "agent_documentation/all_english_tags.md"
EXISTING_TRANSLATIONS_FILE = "data/tag_translations.json"
OUTPUT_FILE = "data/tag_matrix.json"

# Language mappings
LANGUAGES = ["en", "es", "zh", "fr", "de", "pt", "hi", "ar", "ru"]

# Basic translation dictionary for common terms
BASIC_TRANSLATIONS = {
    # Keep some proper nouns in English
    "A00": {"es": "A00", "zh": "A00", "fr": "A00", "de": "A00", "pt": "A00", "hi": "A00", "ar": "A00", "ru": "A00"},
    "Africa": {"es": "África", "zh": "非洲", "fr": "Afrique", "de": "Afrika", "pt": "África", "hi": "अफ्रीका", "ar": "أفريقيا", "ru": "Африка"},
    "African-Studies": {"es": "Estudios Africanos", "zh": "非洲研究", "fr": "Études Africaines", "de": "Afrikastudien", "pt": "Estudos Africanos", "hi": "अफ्रीकी अध्ययन", "ar": "الدراسات الأفريقية", "ru": "Африканские исследования"},
    "Alchemy": {"es": "Alquimia", "zh": "炼金术", "fr": "Alchimie", "de": "Alchemie", "pt": "Alquimia", "hi": "कीमिया", "ar": "الخيمياء", "ru": "Алхимия"},
    "Americas": {"es": "Américas", "zh": "美洲", "fr": "Amériques", "de": "Amerika", "pt": "Américas", "hi": "अमेरिका", "ar": "الأمريكتان", "ru": "Америки"},
    "Ancient Contact": {"es": "Contacto Antiguo", "zh": "古代接触", "fr": "Contact Ancien", "de": "Alter Kontakt", "pt": "Contato Antigo", "hi": "प्राचीन संपर्क", "ar": "الاتصال القديم", "ru": "Древний контакт"},
    "Ancient History": {"es": "Historia Antigua", "zh": "古代历史", "fr": "Histoire Ancienne", "de": "Alte Geschichte", "pt": "História Antiga", "hi": "प्राचीन इतिहास", "ar": "التاريخ القديم", "ru": "Древняя история"},
    "Ancient Wisdom": {"es": "Sabiduría Antigua", "zh": "古代智慧", "fr": "Sagesse Ancienne", "de": "Alte Weisheit", "pt": "Sabedoria Antiga", "hi": "प्राचीन ज्ञान", "ar": "الحكمة القديمة", "ru": "Древняя мудрость"},
    "Animal Intelligence": {"es": "Inteligencia Animal", "zh": "动物智能", "fr": "Intelligence Animale", "de": "Tierische Intelligenz", "pt": "Inteligência Animal", "hi": "पशु बुद्धि", "ar": "الذكاء الحيواني", "ru": "Интеллект животных"},
    "Anthropology": {"es": "Antropología", "zh": "人类学", "fr": "Anthropologie", "de": "Anthropologie", "pt": "Antropologia", "hi": "मानव विज्ञान", "ar": "علم الإنسان", "ru": "Антропология"},
    "Apocrypha": {"es": "Apócrifos", "zh": "伪经", "fr": "Apocryphes", "de": "Apokryphen", "pt": "Apócrifos", "hi": "अपोक्रिफा", "ar": "الأبوكريفا", "ru": "Апокрифы"},
    "Archaeology": {"es": "Arqueología", "zh": "考古学", "fr": "Archéologie", "de": "Archäologie", "pt": "Arqueologia", "hi": "पुरातत्व", "ar": "علم الآثار", "ru": "Археология"},
    "Atlantis": {"es": "Atlántida", "zh": "亚特兰蒂斯", "fr": "Atlantide", "de": "Atlantis", "pt": "Atlântida", "hi": "अटलांटिस", "ar": "أطلانطس", "ru": "Атлантида"},
    "Australian-Dreamtime": {"es": "Tiempo del Sueño Australiano", "zh": "澳洲梦时代", "fr": "Temps du Rêve Australien", "de": "Australische Traumzeit", "pt": "Tempo dos Sonhos Australiano", "hi": "ऑस्ट्रेलियाई स्वप्नकाल", "ar": "زمن الأحلام الأسترالي", "ru": "Австралийское время сновидений"},
    "Bullroarer": {"es": "Rombo", "zh": "牛吼器", "fr": "Rhombe", "de": "Schwirrholz", "pt": "Ronco-Touro", "hi": "बुलरोरर", "ar": "مزمار الثور", "ru": "Гуделка"},
    "Campbell": {"es": "Campbell", "zh": "坎贝尔", "fr": "Campbell", "de": "Campbell", "pt": "Campbell", "hi": "कैंपबेल", "ar": "كامبل", "ru": "Кэмпбелл"},
    "China": {"es": "China", "zh": "中国", "fr": "Chine", "de": "China", "pt": "China", "hi": "चीन", "ar": "الصين", "ru": "Китай"},
    "Chinese-History": {"es": "Historia China", "zh": "中国历史", "fr": "Histoire Chinoise", "de": "Chinesische Geschichte", "pt": "História Chinesa", "hi": "चीनी इतिहास", "ar": "التاريخ الصيني", "ru": "История Китая"},
    "Christopher Columbus": {"es": "Cristóbal Colón", "zh": "克里斯托弗·哥伦布", "fr": "Christophe Colomb", "de": "Christoph Kolumbus", "pt": "Cristóvão Colombo", "hi": "क्रिस्टोफर कोलंबस", "ar": "كريستوفر كولومبوس", "ru": "Христофор Колумб"},
    "Church-History": {"es": "Historia de la Iglesia", "zh": "教会历史", "fr": "Histoire de l'Église", "de": "Kirchengeschichte", "pt": "História da Igreja", "hi": "चर्च का इतिहास", "ar": "تاريخ الكنيسة", "ru": "История Церкви"},
    "Cognitive Science": {"es": "Ciencia Cognitiva", "zh": "认知科学", "fr": "Science Cognitive", "de": "Kognitionswissenschaft", "pt": "Ciência Cognitiva", "hi": "संज्ञानात्मक विज्ञान", "ar": "علم الإدراك", "ru": "Когнитивная наука"},
    "Colonial History": {"es": "Historia Colonial", "zh": "殖民历史", "fr": "Histoire Coloniale", "de": "Kolonialgeschichte", "pt": "História Colonial", "hi": "औपनिवेशिक इतिहास", "ar": "التاريخ الاستعماري", "ru": "Колониальная история"},
    "Consciousness": {"es": "Conciencia", "zh": "意识", "fr": "Conscience", "de": "Bewusstsein", "pt": "Consciência", "hi": "चेतना", "ar": "الوعي", "ru": "Сознание"},
    "Cooperative Breeding": {"es": "Reproducción Cooperativa", "zh": "合作繁殖", "fr": "Élevage Coopératif", "de": "Kooperative Fortpflanzung", "pt": "Reprodução Cooperativa", "hi": "सहकारी प्रजनन", "ar": "التكاثر التعاوني", "ru": "Кооперативное размножение"},
    "Cosmology": {"es": "Cosmología", "zh": "宇宙学", "fr": "Cosmologie", "de": "Kosmologie", "pt": "Cosmologia", "hi": "ब्रह्मांड विज्ञान", "ar": "علم الكونيات", "ru": "Космология"},
    "Creation Stories": {"es": "Historias de Creación", "zh": "创世故事", "fr": "Récits de Création", "de": "Schöpfungsgeschichten", "pt": "Histórias da Criação", "hi": "सृष्टि कहानियां", "ar": "قصص الخلق", "ru": "Истории сотворения"},
    "Cultural Diffusion": {"es": "Difusión Cultural", "zh": "文化传播", "fr": "Diffusion Culturelle", "de": "Kulturelle Diffusion", "pt": "Difusão Cultural", "hi": "सांस्कृतिक प्रसार", "ar": "الانتشار الثقافي", "ru": "Культурная диффузия"},
    "Cultural Evolution": {"es": "Evolución Cultural", "zh": "文化进化", "fr": "Évolution Culturelle", "de": "Kulturelle Evolution", "pt": "Evolução Cultural", "hi": "सांस्कृतिक विकास", "ar": "التطور الثقافي", "ru": "Культурная эволюция"},
    "Daoism": {"es": "Taoísmo", "zh": "道教", "fr": "Taoïsme", "de": "Daoismus", "pt": "Taoísmo", "hi": "ताओवाद", "ar": "الطاوية", "ru": "Даосизм"},
    "Darwin": {"es": "Darwin", "zh": "达尔文", "fr": "Darwin", "de": "Darwin", "pt": "Darwin", "hi": "डार्विन", "ar": "داروين", "ru": "Дарвин"},
    "Deep History": {"es": "Historia Profunda", "zh": "深层历史", "fr": "Histoire Profonde", "de": "Tiefe Geschichte", "pt": "História Profunda", "hi": "गहरा इतिहास", "ar": "التاريخ العميق", "ru": "Глубокая история"},
    "Deep Research": {"es": "Investigación Profunda", "zh": "深度研究", "fr": "Recherche Approfondie", "de": "Tiefenforschung", "pt": "Pesquisa Profunda", "hi": "गहन अनुसंधान", "ar": "بحث عميق", "ru": "Глубокие исследования"},
    "Diffusionism": {"es": "Difusionismo", "zh": "传播主义", "fr": "Diffusionnisme", "de": "Diffusionismus", "pt": "Difusionismo", "hi": "प्रसारवाद", "ar": "الانتشارية", "ru": "Диффузионизм"},
    "Cultural Evolution": {"es": "Evolución Cultural", "zh": "文化进化", "fr": "Évolution Culturelle", "de": "Kulturelle Evolution", "pt": "Evolução Cultural", "hi": "सांस्कृतिक विकास", "ar": "التطور الثقافي", "ru": "Культурная эволюция"},
    "Doctrine and Covenants": {"es": "Doctrina y Convenios", "zh": "教义和圣约", "fr": "Doctrine et Alliances", "de": "Lehre und Bündnisse", "pt": "Doutrina e Convênios", "hi": "सिद्धांत और वाचाएं", "ar": "العقيدة والعهود", "ru": "Учение и Заветы"},
    "EToC": {"es": "EToC", "zh": "EToC", "fr": "EToC", "de": "EToC", "pt": "EToC", "hi": "EToC", "ar": "EToC", "ru": "EToC"},
    "Egypt": {"es": "Egipto", "zh": "埃及", "fr": "Égypte", "de": "Ägypten", "pt": "Egito", "hi": "मिस्र", "ar": "مصر", "ru": "Египет"},
    "Egyptian-myth": {"es": "Mito Egipcio", "zh": "埃及神话", "fr": "Mythe Égyptien", "de": "Ägyptischer Mythos", "pt": "Mito Egípcio", "hi": "मिस्री मिथक", "ar": "الأسطورة المصرية", "ru": "Египетский миф"},
    "Enlightenment": {"es": "Ilustración", "zh": "启蒙运动", "fr": "Siècle des Lumières", "de": "Aufklärung", "pt": "Iluminismo", "hi": "ज्ञानोदय", "ar": "عصر التنوير", "ru": "Просвещение"},
    "Entheogens": {"es": "Enteógenos", "zh": "致幻剂", "fr": "Enthéogènes", "de": "Entheogene", "pt": "Enteógenos", "hi": "एंथियोजेंस", "ar": "المُسكِرات المقدسة", "ru": "Энтеогены"},
    "Epidemiology": {"es": "Epidemiología", "zh": "流行病学", "fr": "Épidémiologie", "de": "Epidemiologie", "pt": "Epidemiologia", "hi": "महामारी विज्ञान", "ar": "علم الأوبئة", "ru": "Эпидемиология"},
    "Esoteric Philosophy": {"es": "Filosofía Esotérica", "zh": "秘教哲学", "fr": "Philosophie Ésotérique", "de": "Esoterische Philosophie", "pt": "Filosofia Esotérica", "hi": "गुप्त दर्शन", "ar": "الفلسفة الباطنية", "ru": "Эзотерическая философия"},
    "Esotericism": {"es": "Esoterismo", "zh": "秘教主义", "fr": "Ésotérisme", "de": "Esoterik", "pt": "Esoterismo", "hi": "गूढ़वाद", "ar": "الباطنية", "ru": "Эзотеризм"},
    "Etymology": {"es": "Etimología", "zh": "词源学", "fr": "Étymologie", "de": "Etymologie", "pt": "Etimologia", "hi": "व्युत्पत्ति", "ar": "علم أصل الكلمات", "ru": "Этимология"},
    "Evolution": {"es": "Evolución", "zh": "进化", "fr": "Évolution", "de": "Evolution", "pt": "Evolução", "hi": "विकास", "ar": "التطور", "ru": "Эволюция"},
    "Evolutionary Theory": {"es": "Teoría Evolutiva", "zh": "进化论", "fr": "Théorie de l'Évolution", "de": "Evolutionstheorie", "pt": "Teoria Evolutiva", "hi": "विकासवादी सिद्धांत", "ar": "نظرية التطور", "ru": "Теория эволюции"},
    "Exploration History": {"es": "Historia de la Exploración", "zh": "探索历史", "fr": "Histoire de l'Exploration", "de": "Entdeckungsgeschichte", "pt": "História da Exploração", "hi": "अन्वेषण इतिहास", "ar": "تاريخ الاستكشاف", "ru": "История исследований"},
    "Feminist Theory": {"es": "Teoría Feminista", "zh": "女权主义理论", "fr": "Théorie Féministe", "de": "Feministische Theorie", "pt": "Teoria Feminista", "hi": "नारीवादी सिद्धांत", "ar": "النظرية النسوية", "ru": "Феминистская теория"},
    "Freemasonry": {"es": "Masonería", "zh": "共济会", "fr": "Franc-maçonnerie", "de": "Freimaurerei", "pt": "Maçonaria", "hi": "फ्रीमेसनरी", "ar": "الماسونية", "ru": "Масонство"},
    "Gender": {"es": "Género", "zh": "性别", "fr": "Genre", "de": "Geschlecht", "pt": "Gênero", "hi": "लिंग", "ar": "الجنس", "ru": "Гендер"},
    "Genetics": {"es": "Genética", "zh": "遗传学", "fr": "Génétique", "de": "Genetik", "pt": "Genética", "hi": "आनुवंशिकता", "ar": "علم الوراثة", "ru": "Генетика"},
    "Gnosticism": {"es": "Gnosticismo", "zh": "诺斯替主义", "fr": "Gnosticisme", "de": "Gnostizismus", "pt": "Gnosticismo", "hi": "ज्ञानवाद", "ar": "الغنوصية", "ru": "Гностицизм"},
    "Greek Philosophy": {"es": "Filosofía Griega", "zh": "希腊哲学", "fr": "Philosophie Grecque", "de": "Griechische Philosophie", "pt": "Filosofia Grega", "hi": "यूनानी दर्शन", "ar": "الفلسفة اليونانية", "ru": "Греческая философия"},
    "Greek-myth": {"es": "Mito Griego", "zh": "希腊神话", "fr": "Mythe Grec", "de": "Griechischer Mythos", "pt": "Mito Grego", "hi": "यूनानी मिथक", "ar": "الأسطورة اليونانية", "ru": "Греческий миф"},
    "Hermeticism": {"es": "Hermetismo", "zh": "赫尔墨斯主义", "fr": "Hermétisme", "de": "Hermetismus", "pt": "Hermetismo", "hi": "हर्मेटिसिज्म", "ar": "الهرمسية", "ru": "Герметизм"},
    "Historiography": {"es": "Historiografía", "zh": "史学", "fr": "Historiographie", "de": "Geschichtsschreibung", "pt": "Historiografia", "hi": "इतिहासलेखन", "ar": "علم التأريخ", "ru": "Историография"},
    "History": {"es": "Historia", "zh": "历史", "fr": "Histoire", "de": "Geschichte", "pt": "História", "hi": "इतिहास", "ar": "التاريخ", "ru": "История"},
    "History of Science": {"es": "Historia de la Ciencia", "zh": "科学史", "fr": "Histoire des Sciences", "de": "Wissenschaftsgeschichte", "pt": "História da Ciência", "hi": "विज्ञान का इतिहास", "ar": "تاريخ العلوم", "ru": "История науки"},
    "Holy-Family": {"es": "Sagrada Familia", "zh": "圣家", "fr": "Sainte Famille", "de": "Heilige Familie", "pt": "Sagrada Família", "hi": "पवित्र परिवार", "ar": "العائلة المقدسة", "ru": "Святое семейство"},
    "Human Evolution": {"es": "Evolución Humana", "zh": "人类进化", "fr": "Évolution Humaine", "de": "Menschliche Evolution", "pt": "Evolução Humana", "hi": "मानव विकास", "ar": "التطور البشري", "ru": "Эволюция человека"},
    "Human Genetics": {"es": "Genética Humana", "zh": "人类遗传学", "fr": "Génétique Humaine", "de": "Humangenetik", "pt": "Genética Humana", "hi": "मानव आनुवंशिकता", "ar": "علم الوراثة البشرية", "ru": "Генетика человека"},
    "Human Origins": {"es": "Orígenes Humanos", "zh": "人类起源", "fr": "Origines Humaines", "de": "Menschliche Ursprünge", "pt": "Origens Humanas", "hi": "मानव मूल", "ar": "أصول البشر", "ru": "Происхождение человека"},
    "Identity": {"es": "Identidad", "zh": "身份", "fr": "Identité", "de": "Identität", "pt": "Identidade", "hi": "पहचान", "ar": "الهوية", "ru": "Идентичность"},
    "Indigenous-Studies": {"es": "Estudios Indígenas", "zh": "土著研究", "fr": "Études Autochtones", "de": "Indigene Studien", "pt": "Estudos Indígenas", "hi": "स्वदेशी अध्ययन", "ar": "الدراسات الأصلية", "ru": "Исследования коренных народов"},
    "Indo‑European": {"es": "Indoeuropeo", "zh": "印欧语系", "fr": "Indo-européen", "de": "Indoeuropäisch", "pt": "Indo-europeu", "hi": "भारत-यूरोपीय", "ar": "الهندو أوروبية", "ru": "Индоевропейский"},
    "Instruments": {"es": "Instrumentos", "zh": "乐器", "fr": "Instruments", "de": "Instrumente", "pt": "Instrumentos", "hi": "वाद्य यंत्र", "ar": "الآلات", "ru": "Инструменты"},
    "Jesus": {"es": "Jesús", "zh": "耶稣", "fr": "Jésus", "de": "Jesus", "pt": "Jesus", "hi": "यीशु", "ar": "يسوع", "ru": "Иисус"},
    "Joseph Smith": {"es": "José Smith", "zh": "约瑟夫·史密斯", "fr": "Joseph Smith", "de": "Joseph Smith", "pt": "Joseph Smith", "hi": "जोसेफ स्मिथ", "ar": "جوزيف سميث", "ru": "Джозеф Смит"},
    "LDS": {"es": "SUD", "zh": "LDS", "fr": "SDJ", "de": "HLT", "pt": "SUD", "hi": "LDS", "ar": "LDS", "ru": "СПД"},
    "Linguistics": {"es": "Lingüística", "zh": "语言学", "fr": "Linguistique", "de": "Linguistik", "pt": "Linguística", "hi": "भाषाविज्ञान", "ar": "علم اللغة", "ru": "Лингвистика"},
    "Linguistic‑Magic": {"es": "Magia Lingüística", "zh": "语言魔法", "fr": "Magie Linguistique", "de": "Sprachliche Magie", "pt": "Magia Linguística", "hi": "भाषाई जादू", "ar": "السحر اللغوي", "ru": "Лингвистическая магия"},
    "Matriarchy Debate": {"es": "Debate del Matriarcado", "zh": "母权制辩论", "fr": "Débat sur le Matriarcat", "de": "Matriarchatsdebatte", "pt": "Debate do Matriarcado", "hi": "मातृसत्ता बहस", "ar": "جدل النظام الأمومي", "ru": "Дебаты о матриархате"},
    "Memory": {"es": "Memoria", "zh": "记忆", "fr": "Mémoire", "de": "Gedächtnis", "pt": "Memória", "hi": "स्मृति", "ar": "الذاكرة", "ru": "Память"},
    "Mesoamerica": {"es": "Mesoamérica", "zh": "中美洲", "fr": "Mésoamérique", "de": "Mesoamerika", "pt": "Mesoamérica", "hi": "मेसोअमेरिका", "ar": "أمريكا الوسطى", "ru": "Мезоамерика"},
    "Mexican History": {"es": "Historia Mexicana", "zh": "墨西哥历史", "fr": "Histoire Mexicaine", "de": "Mexikanische Geschichte", "pt": "História Mexicana", "hi": "मैक्सिकन इतिहास", "ar": "التاريخ المكسيكي", "ru": "История Мексики"},
    "Migration": {"es": "Migración", "zh": "迁移", "fr": "Migration", "de": "Migration", "pt": "Migração", "hi": "प्रवासन", "ar": "الهجرة", "ru": "Миграция"},
    "Mormonism": {"es": "Mormonismo", "zh": "摩门教", "fr": "Mormonisme", "de": "Mormonentum", "pt": "Mormonismo", "hi": "मॉर्मन धर्म", "ar": "المورمونية", "ru": "Мормонизм"},
    "Music": {"es": "Música", "zh": "音乐", "fr": "Musique", "de": "Musik", "pt": "Música", "hi": "संगीत", "ar": "الموسيقى", "ru": "Музыка"},
    "Mystery Cults": {"es": "Cultos Mistéricos", "zh": "神秘教派", "fr": "Cultes à Mystères", "de": "Mysterienkulte", "pt": "Cultos de Mistério", "hi": "रहस्य संप्रदाय", "ar": "الطوائف الغامضة", "ru": "Мистериальные культы"},
    "Mysticism": {"es": "Misticismo", "zh": "神秘主义", "fr": "Mysticisme", "de": "Mystizismus", "pt": "Misticismo", "hi": "रहस्यवाद", "ar": "التصوف", "ru": "Мистицизм"},
    "Myth": {"es": "Mito", "zh": "神话", "fr": "Mythe", "de": "Mythos", "pt": "Mito", "hi": "मिथक", "ar": "الأسطورة", "ru": "Миф"},
    "Mythology": {"es": "Mitología", "zh": "神话学", "fr": "Mythologie", "de": "Mythologie", "pt": "Mitologia", "hi": "पौराणिक कथा", "ar": "الأساطير", "ru": "Мифология"},
    "Narrative": {"es": "Narrativa", "zh": "叙事", "fr": "Récit", "de": "Erzählung", "pt": "Narrativa", "hi": "कथा", "ar": "السرد", "ru": "Повествование"},
    "Neurobiology": {"es": "Neurobiología", "zh": "神经生物学", "fr": "Neurobiologie", "de": "Neurobiologie", "pt": "Neurobiologia", "hi": "न्यूरोबायोलॉजी", "ar": "علم الأحياء العصبي", "ru": "Нейробиология"},
    "Neuroscience": {"es": "Neurociencia", "zh": "神经科学", "fr": "Neurosciences", "de": "Neurowissenschaft", "pt": "Neurociência", "hi": "तंत्रिका विज्ञान", "ar": "علم الأعصاب", "ru": "Нейронауки"},
    "Olmec": {"es": "Olmeca", "zh": "奥尔梅克", "fr": "Olmèque", "de": "Olmeken", "pt": "Olmeca", "hi": "ओल्मेक", "ar": "الأولمك", "ru": "Ольмеки"},
    "Oral Tradition": {"es": "Tradición Oral", "zh": "口述传统", "fr": "Tradition Orale", "de": "Mündliche Tradition", "pt": "Tradição Oral", "hi": "मौखिक परंपरा", "ar": "التقليد الشفهي", "ru": "Устная традиция"},
    "Origins": {"es": "Orígenes", "zh": "起源", "fr": "Origines", "de": "Ursprünge", "pt": "Origens", "hi": "मूल", "ar": "الأصول", "ru": "Происхождение"},
    "Paleolithic": {"es": "Paleolítico", "zh": "旧石器时代", "fr": "Paléolithique", "de": "Paläolithikum", "pt": "Paleolítico", "hi": "पुरापाषाण", "ar": "العصر الحجري القديم", "ru": "Палеолит"},
    "Philosophy": {"es": "Filosofía", "zh": "哲学", "fr": "Philosophie", "de": "Philosophie", "pt": "Filosofia", "hi": "दर्शन", "ar": "الفلسفة", "ru": "Философия"},
    "Polynesia": {"es": "Polinesia", "zh": "波利尼西亚", "fr": "Polynésie", "de": "Polynesien", "pt": "Polinésia", "hi": "पॉलिनेशिया", "ar": "بولينيزيا", "ru": "Полинезия"},
    "Prehistory": {"es": "Prehistoria", "zh": "史前史", "fr": "Préhistoire", "de": "Vorgeschichte", "pt": "Pré-história", "hi": "प्रागैतिहासिक", "ar": "ما قبل التاريخ", "ru": "Доистория"},
    "Pronouns": {"es": "Pronombres", "zh": "代词", "fr": "Pronoms", "de": "Pronomen", "pt": "Pronomes", "hi": "सर्वनाम", "ar": "الضمائر", "ru": "Местоимения"},
    "Pseudoarchaeology": {"es": "Pseudoarqueología", "zh": "伪考古学", "fr": "Pseudo-archéologie", "de": "Pseudoarchäologie", "pt": "Pseudoarqueologia", "hi": "छद्म पुरातत्व", "ar": "علم الآثار الزائف", "ru": "Псевдоархеология"},
    "Psychedelics": {"es": "Psicodélicos", "zh": "迷幻药", "fr": "Psychédéliques", "de": "Psychedelika", "pt": "Psicodélicos", "hi": "साइकेडेलिक्स", "ar": "المُهلِسات", "ru": "Психоделики"},
    "Psychology": {"es": "Psicología", "zh": "心理学", "fr": "Psychologie", "de": "Psychologie", "pt": "Psicologia", "hi": "मनोविज्ञान", "ar": "علم النفس", "ru": "Психология"},
    # Add more translations as needed...
}

def read_english_tags():
    """Read English tags from the markdown file."""
    tags = []
    try:
        with open(ENGLISH_TAGS_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
        
        lines = content.split('\n')
        for line in lines:
            line = line.strip()
            if line.startswith('- '):
                tag = line[2:].strip()
                if tag:
                    tags.append(tag)
        
        print(f"Read {len(tags)} English tags from {ENGLISH_TAGS_FILE}")
        return sorted(tags)
        
    except Exception as e:
        print(f"Error reading English tags: {e}")
        return []

def load_existing_translations():
    """Load existing translations from data/tag_translations.json."""
    try:
        with open(EXISTING_TRANSLATIONS_FILE, 'r', encoding='utf-8') as f:
            existing = json.load(f)
        print(f"Loaded {len(existing)} existing translations")
        return existing
    except Exception as e:
        print(f"Could not load existing translations: {e}")
        return {}

def create_translated_matrix(english_tags):
    """Create a matrix with proper translations for each language."""
    matrix = {}
    existing_translations = load_existing_translations()
    
    for tag in english_tags:
        matrix[tag] = {}
        
        # Always set English
        matrix[tag]["en"] = tag
        
        # Check if we have existing translations
        tag_found = False
        for existing_key, existing_translations_dict in existing_translations.items():
            if existing_key.lower() == tag.lower() or existing_key == tag:
                # Use existing translations
                for lang in LANGUAGES[1:]:  # Skip 'en'
                    if lang in existing_translations_dict:
                        matrix[tag][lang] = existing_translations_dict[lang]
                        tag_found = True
                break
        
        if not tag_found:
            # Check our basic translations
            if tag in BASIC_TRANSLATIONS:
                for lang in LANGUAGES[1:]:  # Skip 'en'
                    if lang in BASIC_TRANSLATIONS[tag]:
                        matrix[tag][lang] = BASIC_TRANSLATIONS[tag][lang]
                    else:
                        matrix[tag][lang] = tag  # Fallback to English
            else:
                # Fallback to English for now (could add machine translation here)
                for lang in LANGUAGES[1:]:  # Skip 'en'
                    matrix[tag][lang] = tag
                print(f"No translation found for: {tag}")
    
    return matrix

def save_translated_matrix(matrix, output_file):
    """Save the translated matrix as JSON."""
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(matrix, f, indent=2, ensure_ascii=False)
        print(f"Translated matrix saved to {output_file}")
        return True
    except Exception as e:
        print(f"Error saving translated matrix: {e}")
        return False

def main():
    print("Tag Translation Matrix Script")
    print("=" * 40)
    
    # Read English tags
    english_tags = read_english_tags()
    if not english_tags:
        print("No English tags found. Exiting.")
        return
    
    print(f"Creating translated matrix for {len(english_tags)} tags across {len(LANGUAGES)} languages")
    
    # Create translated matrix
    matrix = create_translated_matrix(english_tags)
    
    # Save matrix
    if save_translated_matrix(matrix, OUTPUT_FILE):
        print(f"\n✅ Success! Created translated tag matrix")
        print(f"   Output: {OUTPUT_FILE}")
        
        # Show sample
        sample_tag = list(matrix.keys())[0]
        print(f"\n📝 Sample translations for '{sample_tag}':")
        for lang, translation in matrix[sample_tag].items():
            print(f"   {lang}: {translation}")
    else:
        print("❌ Failed to save matrix")

if __name__ == "__main__":
    main() 