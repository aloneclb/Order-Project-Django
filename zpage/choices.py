"""
    App'e ait herhangi bir choices kısmı bu dosyadadır.
"""

class StatusChoices:
    """
        Hakkımızda Durumu İçin Choices
    """
    false_choices = 0
    true_choices = 1
    delete_choices = 2

    CHOICES = (
        #(Database'de Tutulacak Değer, Kullanıcıya gösterilecek değeri)
        (false_choices, "Taslak"),
        (true_choices, "Yayınla"),
        (delete_choices, "Sil"),

    )