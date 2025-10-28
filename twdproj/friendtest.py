import pandas as pd
import matplotlib.pyplot as plt
import os  # <-- Ważne, żeby zaimportować 'os'

# --- POPRAWKA TUTAJ ---
# Ustaw ścieżkę do katalogu, w którym trzymasz pliki CSV
data_dir = 'twdproj\dane_statystyki' 

# Lista bazowych nazw plików
files_list_names = [
    'statystyki-2016.csv', 'statystyki-2017.csv', 'statystyki-2018.csv',
    'statystyki-2019.csv', 'statystyki-2020.csv', 'statystyki-2021.csv',
    'statystyki-2022.csv', 'statystyki-2023.csv', 'statystyki-2024.csv',
    'statystyki-2025.csv'
]

# Standardowe nazwy kolumn, których szukamy
standard_month_cols = [
    'styczeń', 'luty', 'marzec', 'kwiecień', 'maj', 'czerwiec',
    'lipiec', 'sierpień', 'wrzesień', 'październik', 'listopad', 'grudzień'
]
standard_total_cols = ['normalne', 'ulgowe', 'razem']
rows_to_exclude = ['RAZEM', 'Mieszkańcy', 'Zwolnieni', 'Skiturowcy']

all_dfs = []

for file_name in files_list_names:
    try:
        # --- POPRAWKA TUTAJ ---
        # Budowanie pełnej ścieżki do pliku
        file_path = os.path.join(data_dir, file_name)
        
        # Wyciągnij rok z nazwy pliku
        year = int(file_name.split('-')[1].split('.')[0])
        
        # Wczytaj CSV z poprawnej ścieżki
        df = pd.read_csv(file_path, delimiter=';', header=0, skipinitialspace=True)
        
        # Oczyszczanie nazw kolumn
        df.columns = df.columns.str.strip().str.replace('"', '')
        
        # Renaming 'name' column and cleaning it
        if 'name' in df.columns:
            df = df.rename(columns={'name': 'Lokalizacja'})
        else:
            if 'Lokalizacja' not in df.columns:
                first_col_name = df.columns[0]
                df = df.rename(columns={first_col_name: 'Lokalizacja'})

        df['Lokalizacja'] = df['Lokalizacja'].str.strip()
        
        # Usunięcie wierszy podsumowujących
        df = df[~df['Lokalizacja'].isin(rows_to_exclude)]
        
        # Usunięcie wierszy, gdzie lokalizacja jest pusta
        df = df.dropna(subset=['Lokalizacja'])
        
        # Znajdź kolumny, które pasują do naszych standardowych list
        current_month_cols = [col for col in df.columns if col in standard_month_cols]
        current_total_cols = [col for col in df.columns if col in standard_total_cols]
        cols_to_clean = current_month_cols + current_total_cols
        
        # Czyszczenie wartości w kolumnach
        for col in cols_to_clean:
            df[col] = df[col].astype(str).str.replace(r'[\s"]', '', regex=True)
            df[col] = pd.to_numeric(df[col], errors='coerce')
        
        df = df.fillna(0)
        
        df['Rok'] = int(year)
        
        final_cols = ['Rok', 'Lokalizacja'] + current_month_cols + current_total_cols
        final_cols = [col for col in final_cols if col in df.columns]
        df = df[final_cols]
        
        all_dfs.append(df)
        
    except Exception as e:
        # Teraz ten błąd powinien się pojawić tylko jeśli pliku FAKTYCZNIE brakuje
        print(f"Błąd podczas przetwarzania pliku {file_path}: {e}")

# Połącz wszystkie ramki danych
# Ten krok nie powinien już zgłaszać błędu, jeśli jakikolwiek plik zostanie znaleziony
if not all_dfs:
    print("Nie wczytano żadnych danych. Sprawdź ścieżkę 'data_dir' i nazwy plików.")
else:
    full_data = pd.concat(all_dfs, ignore_index=True)

    # Konwersja typów kolumn na liczbowe
    for col in standard_month_cols + standard_total_cols:
        if col in full_data.columns:
            full_data[col] = pd.to_numeric(full_data[col], errors='coerce').fillna(0)

    # Zapisz do CSV
    # Plik wyjściowy zostanie zapisany w katalogu, z którego uruchamiasz skrypt
    output_csv = 'statystyki_TPN_lata_2016-2025_oczyszczone.csv'
    full_data.to_csv(output_csv, index=False)
    print(f"Zapisano połączone dane do '{output_csv}'")
    print("\nOczyszczone i połączone dane (pierwsze 5 wierszy):")
    print(full_data.head())

    # --- Analiza i wykresy ---
    # (Reszta kodu do generowania wykresów jest taka sama)

    # 1. Całkowita liczba odwiedzających w poszczególnych latach
    yearly_totals = full_data.groupby('Rok')['razem'].sum().reset_index()

    print("\nCałkowita liczba odwiedzających rocznie:")
    print(yearly_totals)

    plt.figure(figsize=(10, 6))
    plt.plot(yearly_totals['Rok'], yearly_totals['razem'], marker='o', linestyle='-', color='b')
    plt.title('Całkowita liczba odwiedzających TPN w latach 2016-2025')
    plt.xlabel('Rok')
    plt.ylabel('Liczba odwiedzających (w mln)')
    plt.grid(True, linestyle='--', alpha=0.6)
    from matplotlib.ticker import FuncFormatter
    def millions_formatter(x, pos):
        return f'{x/1e6:.1f} mln'
    plt.gca().yaxis.set_major_formatter(FuncFormatter(millions_formatter))
    plt.xticks(yearly_totals['Rok']) 
    plt.tight_layout()
    plt.savefig('total_visitors_per_year.png')
    print("Zapisano wykres 'total_visitors_per_year.png'")


    # 2. Top 10 najpopularniejszych wejść
    location_totals = full_data.groupby('Lokalizacja')['razem'].sum().sort_values(ascending=False).reset_index()
    top_10_locations = location_totals.head(10)

    print("\nTop 10 lokalizacji (cały okres):")
    print(top_10_locations)

    plt.figure(figsize=(12, 8))
    plt.barh(top_10_locations['Lokalizacja'], top_10_locations['razem'], color='steelblue')
    plt.title('Top 10 najpopularniejszych wejść do TPN (Suma z lat 2016-2025)')
    plt.xlabel('Całkowita liczba odwiedzających (w mln)')
    plt.ylabel('Lokalizacja')
    plt.gca().invert_yaxis()  
    plt.gca().xaxis.set_major_formatter(FuncFormatter(millions_formatter))
    plt.tight_layout()
    plt.savefig('top_10_locations.png')
    print("Zapisano wykres 'top_10_locations.png'")


    # 3. Sezonowość (rozkład miesięczny)
    month_order = standard_month_cols
    existing_month_cols = [col for col in month_order if col in full_data.columns]
    monthly_totals_sum = full_data[existing_month_cols].sum()
    monthly_totals = monthly_totals_sum.reset_index()
    monthly_totals.columns = ['Miesiąc', 'Liczba_odwiedzin']
    monthly_totals['Miesiąc'] = pd.Categorical(monthly_totals['Miesiąc'], categories=month_order, ordered=True)
    monthly_totals = monthly_totals.sort_values('Miesiąc')

    print("\nSuma odwiedzin per miesiąc (wszystkie lata):")
    print(monthly_totals)

    plt.figure(figsize=(12, 7))
    plt.bar(monthly_totals['Miesiąc'], monthly_totals['Liczba_odwiedzin'], color='darkgreen')
    plt.title('Suma odwiedzin w podziale na miesiące (2016-2025)')
    plt.xlabel('Miesiąc')
    plt.ylabel('Liczba odwiedzających')
    plt.xticks(rotation=45, ha='right')
    plt.gca().yaxis.set_major_formatter(FuncFormatter(millions_formatter))
    plt.tight_layout()
    plt.savefig('monthly_seasonality.png')
    print("Zapisano wykres 'monthly_seasonality.png'")


    # 4. Stosunek biletów normalnych do ulgowych
    ticket_type_totals = full_data.groupby('Rok')[['normalne', 'ulgowe']].sum()

    print("\nBilety normalne vs. ulgowe rocznie:")
    print(ticket_type_totals)

    ticket_type_totals.plot(kind='bar', stacked=True, figsize=(11, 7), colormap='viridis')
    plt.title('Stosunek biletów normalnych do ulgowych w latach')
    plt.xlabel('Rok')
    plt.ylabel('Liczba biletów')
    plt.legend(title='Typ biletu')
    plt.xticks(rotation=0)
    plt.gca().yaxis.set_major_formatter(FuncFormatter(millions_formatter))
    plt.tight_layout()
    plt.savefig('ticket_types_per_year.png')
    print("Zapisano wykres 'ticket_types_per_year.png'")

    print("\nGotowe. Wykresy i plik CSV zostały zapisane w katalogu.")