"""
    Sınıfların Veya Formların Choicesları Açıklamaları İle Beraber
    Bu klasördedir.
"""

class StatusChoices:
    """
        Bir ürün veya nesnenin durumu için seçenekler.
    """
    false_choices = 0
    true_choices = 1
    delete_choices = 2

    CHOICES = (
        #(Database'de Tutulacak Değer, Kullanıcıya gösterilecek değeri)
        (false_choices, "Taslak"),
        (true_choices, "Yayında"),
        (delete_choices, "Sil")
    )

class ProductGenderChoices:
    """
        Cinsiyet için choices
    """
    male = 0
    female = 1
    unisex = 2
    child = 3

    CHOICES = (
        #(Database'de Tutulacak Değer, Kullanıcıya gösterilecek değeri)
        (male, "Erkek"),
        (female, "Kadın"),
        (unisex, "Unisex"),
        (child, 'Çocuk')
    )