# User Stories

1. Nazwa
Wpisywanie ocen

2. User Stories:
Jako nauczyciel korzystający z dziennika elektronicznego chcę mieć możliwość wpisywania ocen cząstkowych by na ich podstawie wystawić ocenę końcową.

3. Kryteria akceptacji:
Kryteria Funkcjonalne:
Czy dostęp do ocen danego przedmiotu ma tylko nauczyciel tego przedmiotu?
Czy aplikacja wygeneruje proponowaną ocenę końcową na podstawie ocen cząstkowych i ich wag? 
Czy wystawiane oceny są zgodne ze statutem szkoły i ustawą o systemie oświaty?
 
Kryteria niefunkcjonalne
Czy zapis ocen końcowych trwa szybciej niż 1 sekundę?
Czy można wystawić inną ocenę niż przewiduje to ustawa o systemie oświaty?
 
4. Scenariusze testowe:
Scenariusz 1: Poprawne wystawienie ocen końcowych.
Przyjmując, że nauczyciel wprowadził wszystkie oceny cząstkowe oraz ich wagi oraz że wszystkie oceny końcowe są wpisane, kiedy nauczyciel wybierze opcję Wystaw oceny wtedy oceny zostaną zapisane i staną się widoczne dla uczniów, rodziców uczniów i pozostałych nauczycieli. 

Scenariusz 2: Niepoprawne wystawienie ocen końcowych.
Przyjmując, że nauczyciel pominął jednego ucznia przy wpisywaniu ocen końcowych, kiedy naciśnie przycisk Wystaw oceny Wtedy pojawi się informacja o konieczności wystawienia ocen wszystkim aktywnym uczniom. 




1. Nazwa
Sprawdzanie obecności z generowaniem raportu o frekwencji 

2. User Stories:
Jako nauczyciel korzystający z dziennika elektronicznego chcę mieć możliwość sprawdzenia obecności by na ich podstawie wygenerować raport i sprawdzić frekwencję danego ucznia.

3. Kryteria akceptacji:
Kryteria Funkcjonalne:
Czy dostęp do obecności na danej godzinie w określonej klasie ma tylko nauczyciel, który ma mieć wtedy lekcję z klasą lub osoba, która zastępuje nieobecnego nauczyciela?
Czy aplikacja przewiduje spóźnienie? 
Czy aplikacja powiadomi rodzica o ucieczce ucznia z lekcji?
 
Kryteria niefunkcjonalne
Czy wygenerowanie raportu z frekwencją trwa dłużej niż 2 sekundy?
Czy aplikacja prawidłowo obliczy % udział ucznia w lekcjach z danego przedmiotu?
 
4. Scenariusze testowe:
Scenariusz 1: Poprawne sprawdzenie obecności.
Przyjmując, że nauczyciel zaznaczył odpowiednie pola – obecny/nieobecny ¬– kiedy naciśnie przycisk „Zapisz obecność” wtedy obecność zostanie zapisana i pojawi się komunikat obecność sprawdzona.
Scenariusz 2: Poprawne generowanie raportu frekwencji.
Nauczyciel naciska na przycisk „Generuj raport frekwencji” następnie wybiera danego ucznia i klika „Generuj”, następuje podliczenie frekwencji ucznia na danym przedmiocie i wyświetlenie statystyk obecności/nieobecności usprawiedliwionych/nieobecności nieusprawiedliwionych. 

Scenariusz 3: Niepoprawne sprawdzenie obecności.
Przyjmując, że nauczyciel pominął pola -obecny/nieobecny- przy jednym uczniu, kiedy naciśnie przycisk „Zapisz obecność” wtedy pojawi się komunikat, że należy zaznaczyć jedno pole przy każdym z uczniów. 


1. Nazwa
Sprawdzanie ocen - uczeń

2. User Stories:
Jako uczeń korzystający z dziennika elektronicznego chcę mieć możliwość sprawdzenia ocen.

3. Kryteria akceptacji:
Kryteria Funkcjonalne:
Czy uczeń ma dostęp tylko do swoich ocen?
Czy uczeń dostaje powiadomienie o otrzymaniu nowej oceny? 
Czy uczeń może zobaczyć komentarz nauczyciela do wystawionej ocen?
 
Kryteria niefunkcjonalne
Czy dziennik posiada wersję na urządzenia mobilne?

4. Scenariusze testowe:
Scenariusz 1: Poprawne wyświetlanie ocen.
Uczeń wchodzi w zakładkę „Oceny” i zostają mu wyświetlone jego oceny. Po najechaniu myszką i kliknięciu w daną ocenę zostaje wyświetlony komentarz nauczyciela do wystawionej oceny. 
Scenariusz 2: Poprawność działania powiadomienia o nowej ocenie. 
Nauczyciel wystawia ocenę. Uczeń zostaje powiadomiony mailowo o trzymaniu nowej oceny. Po zalogowaniu się do dziennika widzi ikonę sygnalizującą nową ocenę. Po kliknięciu w przycisk powiadomień zostaje wyświetlona informacja o uzyskanej ocenie oraz przedmiocie, z którego została ona wystawiona.


1. Nazwa
Weryfikacja obecności – usprawiedliwienia. 

2. User Stories:
Jako rodzic korzystający z dziennika elektronicznego chcę mieć możliwość podglądu w frekwencję dziecka by móc usprawiedliwić nieobecności.

3. Kryteria akceptacji:
Kryteria Funkcjonalne:
Czy rodzic widzi frekwencję tylko swojego dziecka?
Czy rodzic może usprawiedliwić nieobecność tylko swojego dziecka? 
Czy rodzic może wcześniej zaplanować i usprawiedliwić nieobecność dziecka?
 
Kryteria niefunkcjonalne
Czy zostaną załadowana prawidłowo cała frekwencja dziecka?

4. Scenariusze testowe:
Scenariusz 1: Poprawne usprawiedliwienie nieobecności.
Rodzic zaznacza nieusprawiedliwione nieobecności dziecka klika na przycisk „Usprawiedliw” zostanie wyświetlone okno, gdzie należy wpisać komentarz dla wychowawcy. Następnie naciska „Prześlij”, zostaje wyświetlona informacja o przesłaniu usprawiedliwienia do wychowawcy. 
Scenariusz 2: Niepoprawne usprawiedliwienie.
Rodzic nie zaznacza żadnej nieobecności dziecka, klika w przycisk „Usprawiedliw” zostaje wyświetlony komunikat o konieczności zaznaczenia co najmniej jednej nieusprawiedliwionej godziny dziecka. 
Scenariusz 3: Poprawne planowanie nieobecności dziecka.
Rodzic klika w przycisk „Poinformuj o nieobecności” wybiera zakres dat następnie naciska przycisk „Prześlij do wychowawcy” zostaje wyświetlone okno do wpisania komentarza. Wpisuje tekst i naciska „ok”. Informacje o nieobecności zostają zapisane oraz komentarz zostaje przesłany do wychowawcy. 



1. Nazwa
Usprawiedliwienia – wychowawca.

2. User Stories:
Jako wychowawca klasy korzystający z dziennika elektronicznego chcę mieć możliwość odebrania usprawiedliwienia od rodzica by móc zaakceptować i usprawiedliwić nieobecność.

3. Kryteria akceptacji:
Kryteria Funkcjonalne:
Czy wychowawca może zobaczyć wszystkie nieobecności swojej klasy?
Czy wychowawca otrzymuje powiadomienie o przesłaniu usprawiedliwienia przez rodzica? 
Czy wychowawca może usprawiedliwić godziny swojej klasy?
Czy wychowawca może napisać wiadomość do rodzica w celu wyjaśnienia nieobecności ucznia?

Kryteria niefunkcjonalne
Czy podgląd nieobecności jest czytelny?
Czy nieobecności ładują się w mniej niż 1sekundę?

4. Scenariusze testowe:
Scenariusz 1: Poprawne usprawiedliwienie nieobecności.
Nauczyciel dostaje informację o przesłanym usprawiedliwieniu od rodzica danego dziecka. Klika w ikonę powiadomień następnie wybiera nową wiadomość. Zostaje załadowany okno z tekstem usprawiedliwienia. Po zweryfikowaniu i zaakceptowaniu usprawiedliwienia naciska przycisk „zatwierdź”. Zostaje zmieniona nieobecność nieusprawiedliwiona na usprawiedliwioną oraz wyświetla się informacja o pomyślnym wykonaniu akcji.
Scenariusz 2: Poprawne wysłanie wiadomości.
Wychowawca wybiera danego ucznia oraz zaznacza nieusprawiedliwione godziny, naciska przycisk „Kontakt z rodzicem”. Pojawia się okno do wpisania wiadomości, po uzupełnieniu treści naciska „wyślij” Wiadomość zostaje przekazana do rodzina oraz wyświetla się napis o prawidłowym przesłaniu informacji. 



1. Nazwa
Weryfikacja nauczycieli

2. User Stories:
Jako dyrektor szkoły, która korzysta z dziennika elektronicznego chcę mieć możliwość wygenerowania raportu o nieuzupełnionych tematach i nie sprawdzonych obecnościach przez nauczycieli by móc wykonać ocenę pracownika szkoły.

3. Kryteria akceptacji:
Kryteria Funkcjonalne:
Czy dyrektor ma wgląd do wszystkich klas?
Czy dyrektor może przeglądać wpisane tematy lekcji? 
Czy dyrektor może przeglądać wszystkie nieobecności?
Czy dyrektor może wygenerować raport z zaznaczonymi niewypełnionymi danymi przez danego nauczyciela?
Czy dyrektor może przesłać informację do wszystkich nauczycieli naraz? 

Kryteria niefunkcjonalne
Czy raport jest czytelny?
Czy raport semestralny generuje się w mniej niż 2 sekundy?

4. Scenariusze testowe:
Scenariusz 1: Poprawne generowanie raportu.
Dyrektor wchodzi w funkcję generowania raportu, wybiera nauczyciela i klika przycisk „Generuj”. Dane zostają pobrane i przedstawione w formie graficznej.
Scenariusz 2: Niepoprawne generowanie raportu.
Dyrektor wchodzi w funkcję generowania raportu, nie wybiera nauczyciela przycisk „generuj” jest nieaktywny. 
Scenariusz 3: Wysłanie wiadomości.
Dyrektor wybiera opcję „wiadomość do wszystkich nauczycieli”, w polu które się pojawi wpisuje treść zawiadomienia. Naciska na przycisk wyślij. Informacja zostaje przekazana do wszystkich nauczycieli uczących w szkole. 

