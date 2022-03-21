Projektplan

Tony Streng 432005
Albert Rehnberg 594011
Vilhelm Nurmi 648543

Plan
  Vår hemsida kommer ha en framsida som syns då man först öppnar hemsidan. Från framsidan kan man rakt trycka sig vidare till inloggning, se spel som man kan ladda ner (reklamfönster med t.ex. AJAX), söka spel och se förslag på populära spel. Framsidan ska ha ett navigationsfält med en sökfunktion, en knapp för att logga in på sin profil, en hem-knapp, alternativ för språk, som extra funktionalitet, och en lista på kategorier via en kategori-knapp. Kategorierna skall grupperas baserat på spelens gemensamma egenskaper, exempelvis tower defense i en kategori. Egenskaperna kan  grupperas med hjälp av tags i en databas dit alla nya spel laddas upp (python-kod) och varje kategori skall inkludera alla spel som taggen stämmer in på. Spel kan ha ett flertal tags som beskriver de.

  På Inloggningssidan loggar man in till sin användare, där man sedan kan se och uppdatera sin information. Där syns vad man har laddat ner, eller om man är en developer också spel som man laddat upp. Där finns också ens profilbild, namn och nationalitet, samt betalningsinformation.

  Från sökfältet kommer man till en sida som visar sökresultaten. Sidan har en matris med resultat för spel och ett till sökresultat för personer på sidan (ifall man sökt på utvecklare och inte spel, eller vice versa) och dessutom en större ruta där man kan göra nya sökningar. Sökmotorn går troligen lättast att bygga med Javascript, och med jQuery hoppas vi få en lite snyggare kod.

  Alla spel som syns på sidan skall också gå att spela. Från framsidan, profilsidan, söksidan etc. skall man kunna öppna spel och börja spela, om man har köpt spelen. Annars blir man ombedd att köpa spelet för att fortsätta. Köpta spel syns på ens profil, och därifrån kan man också lätt öppna och spela alla spel man har köpt. Spelen som öppnas är endast ett popup-fönster med spelet i. I spelen kan man också göra mikrobetalningar; och eftersom man har registrerat ett bankkort som betalningsinformation, så dyker det upp ett popup-fönster som frågar om man vill godkänna transaktionen, och om man gör det så dras pengarna från kortet. Spelen kommer i färdiga “paket” inkluderat spelets kod och referenser, så att nya spel kan grupperas sida vid sida med gamla spel. Spelen är kodade med JavaScript och spelets detaljer kan till exempel vara ett objekt gjort i JSON.

  Spelen ska kunna skicka meddelanden till modersidan för att sidan ska kunna uppdatera en “high score”-lista på varje spel. Spelen skall också gå att spara halvvägs och fortsätta från varifrån man blev. Detta går antagligen lättast att göra med ett simpelt JSON-meddelande som lagras på modersidan och som sedan gör så att spelet återupptas senare. Spelresultat skall också gå att publicera på t.ex. Facebook (kräver att man är inloggad)
  Vi kommer att genomföra projektet genom att träffas minst ett par gånger i veckan och föra projektet framåt. Utöver det är det upp till var och en att koda/söka information mellan mötena, och arbetet kommer vara uppdelat i någon mån, så att alla åtminstone har sin egna del att jobba på. För projektets tidtabells del så kommer vi se till att projektet har en struktur då ca 1/4 av tiden har gått. Halvvägs in så vill vi gärna ha en hemsida som redan gör enkla saker och är tillräckligt bra för att det ska gå att testa och förbättra saker. Med en kvart av projekttiden kvar så kommer vi börja koncentrera oss på detaljer samt förbereda en presentation.

Views med riktgivande innehåll:
  Framsida:
    Skapa nytt konto
    Kvadrater med spelikoner (+ reklam)
    Spel arrangerade enligt kategori
    Logga in- fält
    Sökfält
    Liknande och rekommenderade spel enligt sökning och inköp

Search result-sida:
  Spel som matchar sökningen
  Tidigare sökningar
  Spel som är liknande till sökta spelet/sökning
  Reklam

Spelsida:
  Spel
  Länk till skaparens sida
  Rekommendationer till  spel som andra som spelat spelet gillat
  Kommentarsfält
  Ge betyg för spelet

Användarens personliga sida:
  Köpta spel
  Favoriter
  Kontoinformation
  Ställe att editera information och betalningsinformation

Modeller:

Användardatabas som inkluderar:
  Användar-id
  Lista över köpta spel
  Lösenordshash

Speldatabas:
  Spelkod
  Uppladdare
  Beskrivning
  Beskrivande tags

  
 Slutet av kursen, pohdiskelu:
Vi lyckades implementera de flesta funktioner som vi funderade på i planerings fasen. I början hade vi lite problem med hur det lönar sig att börja när det finns absolut ingenting.
Framsida:							GJORD GANSKA LÅNGT ENLIGT PLANEN
  Skapa nytt konto 													DONE
  Kvadrater med spelikoner (+ reklam)								NOT DONE
  Spel arrangerade enligt kategori									ANPASSAT
  Logga in- fält													DONE
  Sökfält															DONE
  Liknande och rekommenderade spel enligt sökning och inköp			NOT DONE

Search result-sida:					ANNORLUNDA ÄN VI PLANERAT
  Spel som matchar sökningen										DONE
  Tidigare sökningar												NOT DONE
  Spel som är liknande till sökta spelet/sökning					NOT DONE
  Reklam															NOT DONE

Spelsida:							PÅ SPELSIDAN KAN MAN ENDAST SPELA SPELET
  Spel																DONE
  Länk till skaparens sida											NOT DONE
  Rekommendationer till  spel som andra som spelat spelet gillat	NOT DONE
  Kommentarsfält													NOT DONE
  Ge betyg för spelet												NOT DONE

Användarens personliga sida:		VÅRA PLANER ÄNDRADES ENLIGT BETALNINGSINFO
  Köpta spel														DONE
  Favoriter															NOT DONE
  Kontoinformation													NOT DONE
  Ställe att editera information och betalningsinformation			DONE

Modeller:							VÅRA MODELLER BLEV VÄLDIGT LÅNGT SOM PLANERAT

Användardatabas som inkluderar:
  Användar-id														DONE
  Lista över köpta spel												DONE
  Lösenordshash														DONE

Speldatabas:
  Spelkod															DONE
  Uppladdare														DONE	
  Beskrivning														DONE
  Beskrivande tags													NOT DONE
  
 Personlig poängsättning:
	Authentication: 200
			email verification
			använder sig av utomstående tjänster
	
	Basic player functionalities: 300
			spel kan köpas via kursens betalningssida
			spel som inte är köpta går inte att köpas
			det finns både en allmän spelsida, top games och search funktion
			
	Basic developer functionalities: 300
			developern kan lägga upp spel och avgöra priset, modifiera
			endast specifika developern kan editera sitt spel
			enskilda spels information kan hittas av developern
	
	Game/service interaction: 200
			spelarens highscore publiceras på hemsidan 
			avslutas spelet mitt i går det att via JSonp fortsätta där man senast blev
			
	Quality of work: 100
			Kommentarer är utlagda i koden så att man enkelt kan gölja med vilka funktioner gör vad och redigeras ifall det måste
			vi har spenderat mycket tid att fösöka göra arbetet snyggt via bootstrap
			
	Save/load and resolution feature: 100
			spelet kommer ihåg dina resultat ifall man slutar mitt i
			iframen anpassar sig enligt vad spelet vill ha /behöver
			
	3rd party login: 100
			man kan logga in sig via gmail/google +
		
	Own game: 100
			vi har ett pong spel färdigt på hemsidan
			
	mobile friendly: 25
			spelen anpassar sig enligt telefon så de blir svåra men det borde gå att spela
			
	Restful API: 50
			alla spel kan hittas på hemsidan och beroende var man söker anpassar de sig enligt mest spelade eller title