# INSTRUCTIONS

# Translate the text and write it between the "
# EXAMPLE:      original    ->  "This text is in english: value {0}" 
#               translation ->  "Aquest text està en anglès: valor {0}"

# So it would look like: "ORIGINAL_TEXT" : "TRANSLATED_TEXT",


# If you see sth like {0}, {1}, maintain it on the translated sentence
# Meke special attention to elements like ":", etc.

lang2_7_bis = {
    "Use a custom font": "Anvend en brugerdefineret font",
    "Use a custom font size": "Anvend en brugerdefineret skrifttype størrelse",
    "Enable hide when multi-monitor fullscreen apps are running": "Aktiver skjul når multi-skærm fuldskærm apps kører",
    "<b>{0}</b> needs to be enabled to change this setting": "<b>{0}</b> skal være aktiveret for at ændre denne indstilling",
    "<b>{0}</b> needs to be disabled to change this setting": "<b>{0}</b> skal være deaktiveret for at ændre denne indstilling",
}

lang2_7 = lang2_7_bis | {
    " (This feature has been disabled because it should work by default. If it is not, please report a bug)": "(Denne funktion er bleven deaktiveret fordi den bør funktionere som standard. Hvis ikke den er, så venligst rappertere fejlen ",
    "ElevenClock's language": "ElevenClock's sprog"
}

lang2_6 = lang2_7 | {
    "About Qt6 (PySide6)": "Om Qt6 (Pyside6)",
    "About": "Om",
    "Alternative non-SSL update server (This might help with SSL errors)": "Alternativ ikke-SSL opdaterings server (Dette kan muligvis hjælpe med SSL fejl)",
    "Fixes and other experimental features: (Use ONLY if something is not working)": "Fejlretininger og andre eksperimentele funktioner (Må KUN bruges hvis noget ikke virker) ",
    "Show week number on the clock": "Vis uge nummer på uret",
}

lang2_5 = lang2_6 | {
    "Hide the clock when RDP Client or Citrix Workspace are running": "Skjul uret når RDP klienten eller Citrix Workspace kører",
    "Clock Appearance:": "Urets udseende",
    "Force the clock to have black text": "Tving uret til at have sort tekst",
    " - It is required that the Dark Text checkbox is disabled": "-Det er påkrævet at Dark text checkboksen er deaktiveret",
    "Debbugging information:": "Fejlretnings information",
    "Open ElevenClock's log": "Åben ElevenClocks log",deactivated
}

lang2_4 = lang2_5 | {
    # Added text in version 2.4
    "Show the clock on the primary screen (Useful if clock is set on the left)": "Vis uret på den primære skærm (Værdifuldt hvis uret er sat til venstre)",
    "Show weekday on the clock"  :"Vis hverdagen på uret",
}

lang2_3 = lang2_4 | {
    #Context menu
    "ElevenClock Settings"      :"ElevenClock Indstillinger", # Also settings title
    "Reload Clocks"             :"Genindlæs",
    "ElevenClock v{0}"          :"ElevenClock v{0}",
    "Restart ElevenClock"       :"Genstart",
    "Hide ElevenClock"          :"Skjul ElevenClock",
    "Quit ElevenClock"          :"Afslut ElevenClock",
    
    #General settings section
    "General Settings:"                                                                 :"Generelle Indstillinger",
    "Automatically check for updates"                                                   :"Automatisk tjek for opdateringer",
    "Automatically install available updates"                                           :"Automatisk installerer tilgængelige",
    "Enable really silent updates"                                                      :"Aktiver rigtig stille opdateringer",
    "Bypass update provider authenticity check (NOT RECOMMENDED, AT YOUR OWN RISK)"     :"Omgå opdaterings leverandør autenticitet tjek (IKKE ANBEFALET, PÅ EGET RISIKO ",
    "Show ElevenClock on system tray"                                                   :"Vis ElevenClock på system bakken",
    "Alternative clock alignment (may not work)"                                        :"Alternativ ur justering",
    "Change startup behaviour"                                                          :"Ændre opstarts opførsel",
    "Change"                                                                            :"Ændre",
    "<b>Update to the latest version!</b>"                                             :"<b>Opdater til den seneste version</b>",
    "Install update"                                                                    :"Installer opdatering",
    
    #Clock settings
    "Clock Settings:"                                              :"Ur Indstillinger",
    "Hide the clock in fullscreen mode"                            :"Skjul uret i fuldskærems modus",
    "Hide the clock when RDP client is active"                     :"Skjul uret når RDP klient er aktiv",
    "Force the clock to be at the bottom of the screen"            :"Tving uret til at være i bunden af skærmen",
    "Show the clock when the taskbar is set to hide automatically" :"Vis uret når systembakken er sat til at skjul automatisk",
    "Fix the hyphen/dash showing over the month"                   :"Ret op på bindestregen vises over måneden",
    "Force the clock to have white text"                           :"Tving uret til at have hvid tekst",
    "Show the clock at the left of the screen"                     :"Vis uret til venstre for skærmen",
    
    #Date & time settings
    "Date & Time Settings:"                             :"Tid og dato indtillinger",
    "Show seconds on the clock"                         :"Vis sekunder på uret",
    "Show date on the clock"                            :"Vis dato på uret",
    "Show time on the clock"                            :"Vis tid på uret",
    "Change date and time format (Regional settings)"   :"Ændre tid og dato format (Regionelle indstillinger)",
    "Regional settings"                                 :"Regionalle indstillinger",
    
    #About the language pack
    "About the language pack:"                  :"Om sprog pakken",
    "Translated to English by martinet101"      :"Oversat til Dansk af Kerim Katica (Pubp-Proff)", # Here, make sute to give you some credits:  Translated to LANGUAGE by USER/NAME/PSEUDONYM/etc. 
    "Translate ElevenClock to your language"    :"Oversæt ElevenClock til dit sprog",
    "Get started"                               :"Kom igang",
    
    #About ElevenClock
    "About ElevenClock version {0}:"            :"Om ElevenClock version {0}:",
    "View ElevenClock's homepage"               :"Vis ElevenClocks hjemmeside",
    "Open"                                      :"Åben",
    "Report an issue/request a feature"         :"Rapporter en fejl/anmod om en funktion ",
    "Report"                                    :"Reapport",
    "Support the dev: Give me a coffee☕"       :"Støt udvikleren : Giv en kop kaffe",
    "Open page"                                 :"Åben siden",
    "Icons by Icons8"                           :"Ikoner af Icons8", # Here, the word "Icons8" should not be translated
    "Webpage"                                   :"Hjemmeside",
    "Close settings"                            :"Luk indstillinger",
    "Close"                                     :"Luk",
}

lang = lang2_3
