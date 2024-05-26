# napišite program koji kreira akorde na osnovu početnog tona, odnosno note.
# pojašnjenje: 
# akord se sastoji od tri tona koji se mogu ponavljati
# durski akord čine: početni ton, 4. ton, te 7. ton, označava se samo velikim slovom početnog tona ili velikim slovom početnog tona uz dodatak dur
# molski akord čine: početni ton, 3. ton, te 7. ton, označava se 
#program mora ispisati durski i molski akord unesenog tona
#glazbena abeceda: C, C#, D, D#, E, F, F#, G, G#, A, A#, B
# Primjer: unesite ton: C
# Ispis: Durski akord: C, E, G
#           Molski akord: C, D#, 

#GPT prompt:
# #kreiraj program koji će od korisnika tražiti da unese notu iz glazbene abecede (C, C#, D, D#, E, F, F#, G, G#, A, A#, B), te na temelju te note treba isprintati dur ili mol akord.
# durski akord čine: početni ton, četvrti ton, te sedmi ton.
# molski akord čine: početni ton, treći ton, te sedmi ton

# def pimp_my_akord(nota):
#     tonovi = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
# tonovi.extent(notes)
#     dur = [nota, tonovi[(tonovi.index(nota) + 4) % 12], tonovi[(tonovi.index(nota) + 7) % 12]]
#     mol = [nota, tonovi[(tonovi.index(nota) + 3) % 12], tonovi[(tonovi.index(nota) + 7) % 12]]
#     return dur, mol

# nota = input("Unesi notu: ")

# dur, mol = pimp_my_akord(nota)

# print(f"Durski akord: {dur}")
# print(f"Molski akord: {mol}")


###############################

# drugi način


notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
def get_note(index):

    return notes[index % len(notes)]

def get_nth_note(note, n):
    idx=notes.index(note)

    return notes[(idx + n) % len(notes)]

def get_major_chord(note):
    return note, get_nth_note(note, 4), get_nth_note(note, 7)

def get_minor_chord(note):
    return note, get_nth_note(note, 3), get_nth_note(note, 7)


# def get_major_chord(note):
#     major_chord = [note, notes[(notes.index(note) + 4) % len(notes)], notes[(notes.index(note) + 7) % len(notes)]]
#     return major_chord

# def get_minor_chord(note):
#     minor_chord = [note, notes[(notes.index(note) + 3) % len(notes)], notes[(notes.index(note) + 7) % len(notes)]]
#     return minor_chord

note = input("Unesite željeni ton: ")

major_chord = get_major_chord(note)
minor_chord = get_minor_chord(note)


print(f"durski akord: {major_chord}\n"
      f"molski akord: {minor_chord}")