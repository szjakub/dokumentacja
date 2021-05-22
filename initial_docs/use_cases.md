# Use Cases
Nazwa: Sprawdzanie Obecności
Identyfikator: SO
Aktorzy: Nauczyciel, uczeń, rodzic
Udziałowcy/Zainteresowani:
•	Nauczyciel oczekuje szybkiego i skutecznego sprawdzenia obecności oraz wpisania tematu lekcji, czas wykonania tej operacji decyduje o pozostałym czasie do przeprowadzenia lekcji
•	Rodzic oczekuje informacji nieobecności dziecka
•	Dyrektor szkoły oczekuje wykonywania obowiązków przez podwładnych 
Krótki opis: Realizacja sprawdzania obecności
Warunki wstępne: Nauczyciel musi posiadać odpowiednio przypisaną lekcję (godzinę i klasę). Uczniowie muszą być przypisani do odpowiedniej klasy. Rodzic musi być przypisany do co najmniej jednego dziecka. 
Warunki końcowe: Obecność zarejestrowana. Rodzice powiadomieni.
Główny przepływ zdarzeń: 
1.	Nauczyciel rozpoczyna nową lekcję
2.	Nauczyciel wybiera odpowiednią lekcję 
3.	System prezentuje listę uczniów z odpowiedniej klasy
4.	Nauczyciel wprowadza informację o obecności/nieobecności
5.	System rejestruje informacje 
6.	System przekazuje komunikaty o nieobecności do rodziców.
Alternatywne przepływy zdarzeń:
5a. Uczeń się spóźnił:
1.	Nauczyciel otwiera edycję obecności
2.	Nauczyciel poprawia przy odpowiednim uczniu nieobecność na spóźnienie
3.	System rejestruje edycję 
4.	System przekazuje komunikat do rodzica
Specjalne wymagania: Bramka SMS do wysyłania powiadomień 









Nazwa: Wystawianie ocen
Identyfikator: WO
Aktorzy: Nauczyciel, uczeń, rodzic
Udziałowcy/Zainteresowani:
•	Nauczyciel oczekuje szybkiego i skutecznego wprowadzenia ocen 
•	Rodzic oczekuje informacji ocenach dziecka
•	Dyrektor szkoły oczekuje wykonywania obowiązków przez podwładnych 
•	Uczeń oczekuje informacji o zdobytej ocenie
Krótki opis: Realizacja wpisywania ocen
Warunki wstępne: Nauczyciel musi posiadać odpowiednio przypisaną klasę. Uczniowie muszą być przypisani do odpowiedniej klasy. Rodzic musi być przypisany do co najmniej jednego dziecka. 
Warunki końcowe: Oceny zarejestrowane. Rodzice powiadomieni. Uczniowie powiadomieni.
Główny przepływ zdarzeń: 
1.	Nauczyciel rozpoczyna wpisywanie ocen
2.	Nauczyciel wybiera odpowiednią klasę 
3.	System prezentuje listę uczniów z odpowiedniej klasy
4.	Nauczyciel wprowadza informację o ocenach wraz z komentarzem
5.	System rejestruje informacje 
6.	System przekazuje komunikaty o wprowadzeniu nowej oceny do uczniów i do rodziców
Alternatywne przepływy zdarzeń:
1a. Nauczyciel wpisuje oceny z poprawy:
1.	Nauczyciel otwiera oceny klasy i wybiera opcję „poprawy”
2.	Nauczyciel wybiera odpowiednią klasę 
3.	System prezentuje listę uczniów z odpowiedniej klasy
4.	Nauczyciel wprowadza informację o ocenach wraz z komentarzem
5.	System rejestruje informacje 
6.	System przekazuje komunikaty o wprowadzeniu nowej oceny do uczniów i do rodziców
Specjalne wymagania: Bramka SMS do wysyłania powiadomień 








Nazwa: Generowanie raportu na wywiadówkę 
Identyfikator: GRW
Aktorzy: Nauczyciel, wychowawca 
Udziałowcy/Zainteresowani:
•	Nauczyciel oczekuje szybkiego i skutecznego wygenerowania raportów
•	Dyrektor szkoły oczekuje wykonywania obowiązków przez podwładnych 
Krótki opis: Realizacja generowania raportów dla rodziców na wywiadówkę w formie do wydruku.
Warunki wstępne: Wychowawca musi posiadać odpowiednio przypisaną klasę. Uczniowie muszą mieć odpowiednio uzupełnione listy ocen i obecności. 
Warunki końcowe: Średnia ocen policzona. Procentowa frekwencja w lekcjach policzona. Raport w formie graficznej wygenerowany. Raport wydrukowany.
Główny przepływ zdarzeń: 
1.	Wychowawca rozpoczyna generowanie raportu dla rodzica każdego z uczniów
2.	System prezentuje listę uczniów z odpowiedniej klasy
3.	Wychowawca wybiera ucznia i wybiera generowanie raportu
4.	System odczytuje z bazy informacje, liczy średnią ocen, liczy % udział ucznia w lekcjach.
5.	System generuje raport i wyświetla go w formie graficznej.
6.	Nauczyciel weryfikuje czy wszystkie dane są przedstawione w raporcie i klika opcję drukuj.
7.	System przesyła do drukarki raport.
8.	Drukarka drukuje raport.
Nauczyciel powtarza kroki 3-8 do momentu wygenerowania raportu dla każdego ucznia.
9.	Nauczyciel wybiera opcję „generowanie raportu klasy’
10.	System odczytuje informację o wszystkich uczniach w klasie, przelicza średnią klasy i frekwencję klasy.
11.	System generuje i wyświetla raport w formie graficznej.
12.	Nauczyciel wybiera opcję wydruku.
13.	System przesyła informację do drukarki
14.	Drukarka drukuje
Alternatywne przepływy zdarzeń:
5a. Występuje błąd przy generowaniu raportu – nie wszystkie oceny są uzupełnione:
1.	System wyświetla informację o brakującej ocenie i wskazuje nauczyciela, który nie wpisał oceny
2.	Wychowawca przesyła wiadomość do nauczyciela z prośbą o wpisanie oceny.
3.	Nauczyciel wpisuje ocenę
4.	Wychowawca generuje ponownie raport.
11a. Występuje błąd przy generowaniu raportu – nie wszystkie oceny są uzupełnione:
1.	System wyświetla informację o brakującej ocenie i wskazuje nauczyciela, który nie wpisał oceny
2.	Wychowawca przesyła wiadomość do nauczyciela z prośbą o wpisanie oceny.
3.	Nauczyciel wpisuje ocenę
4.	Wychowawca generuje ponownie raport.

Specjalne wymagania: Drukarka. 


Nazwa: Plan lekcji
Identyfikator: PL
Aktorzy:  Uczeń
Udziałowcy/Zainteresowani:
•	Uczeń oczekuje szybkiego sprawdzenia planu godzin wraz z informacją o zmianie Sali i zastępstwie/nieobecności nauczyciela
Krótki opis: Sprawdzanie planu lekcji
Warunki wstępne: Uczeń musi być przypięty do odpowiedniej klasy. Plan lekcji musi być utworzony dla danej klasy. 
Warunki końcowe: Uczeń uzyskał informację o przedmiocie, klasie i nauczycielu który poprowadzi lekcję. 
Główny przepływ zdarzeń: 
1.	Uczeń otwiera Plan lekcji
2.	System weryfikuje do jakiej klasy i grupy jest uczeń przypisany.
3.	System wczytuje przypisany do danej klasy i grupy podział godzin
4.	System przedstawia podział godzin w formie graficznej
Alternatywne przepływy zdarzeń:
3a. System wczytuje informację o nieobecności nauczyciela:
1.	System przedstawia podział godzin w formacie graficznej wraz z informacją o zastępstwie/odwołaniu zajęć
Specjalne wymagania: - 







Nazwa: Wprowadzenie nowego ucznia
Identyfikator: NU
Aktorzy:  Administrator
Udziałowcy/Zainteresowani:
•	Administrator oczekuje szybkiego i bezproblemowego dodania nowego ucznia do dziennika.
Krótki opis: Dodawanie nowego ucznia
Warunki wstępne: Podanie o przyjęcie ucznia do szkoły musi być rozpatrzone pozytywnie. Administrator musi mieć odpowiednie uprawnienia do tworzenia nowego konta w dzienniku. Sekretariat musi przygotować odpowiednie dokumenty.
Warunki końcowe: Uczeń ma utworzone konto w dzienniku wirtualnym. Rodzic ucznia ma utworzone konto w dzienniku wirtualnym. Uczeń jest przypięty do klasy.
Główny przepływ zdarzeń: 
1.	Administrator otrzymuje dokumenty i przechodzi w systemie do dodawania nowego konta.
2.	System wyświetla formularz dodawania ucznia.
3.	Administrator wprowadza wszystkie dane i zatwierdza formularz.
4.	System generuje login i hasło startowe dla ucznia, generuje login i hasło startowe dla rodzica, system zapisuje dane.
5.	System wyświetla informacje o pomyślnym utworzeniu kont dla ucznia i rodzica oraz wyświetla informację o loginach i hasłach startowych.
6.	Administrator drukuje informację o loginach i hasłach.
7.	Administrator otwiera edycję klasy.
8.	System wyświetla listę uczniów danej klasy.
9.	Administrator przypina nowego ucznia i zatwierdza zmiany.
10.	System zapisuje zmiany i przesyła informację o edycji do wychowawcy danej klasy.
Alternatywne przepływy zdarzeń:
3a. System zweryfikował błędnie wprowadzone informacje:
1.	System wyświetla alert o błędnie wprowadzonych danych.
2.	System wyświetla ponownie formularz z wpisanymi przez admina danymi.
3.	Administrator sprawdza i poprawia błędy.
Specjalne wymagania: Drukarka. Konieczność posiadania adresu email przez ucznia i nauczyciela. 
 
