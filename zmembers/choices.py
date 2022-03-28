"""
    Sınıfların Veya Formların Choicesları Açıklamaları İle Beraber
    Bu klasördedir.
"""

class GenderChoices:
    """
        Cinsiyet için choices
    """
    male = 0
    female = 1
    others = 2

    CHOICES = (
        #(Database'de Tutulacak Değer, Kullanıcıya gösterilecek değeri)
        (male, "Erkek"),
        (female, "Kadın"),
        (others, "Diğerleri")
    )