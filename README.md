# Indeed_Web_Scraping

Als Student weis man oft nicht, welche Kentnisse für den Arbeitsmarkt relevant sind. Da ich mich für den Bereich Data Engineering interessiere, die Anzahl an Frameworks und Lösungen dort aber kontnuirtlich zuzunehmen scheint, wollte ich herausfinden was am gefragtesten auf dem Arbeitsmarkt ist. 
Aus diesem Grund habe ich einen Web-Scraper programmiert, welcher die häufigsten Keywords aus 450 Stellenzeigen als Data Engineer filtert. 

Dieser Loopt durch 30 Seiten an relevanten Stellenanzeigen und speichert alle Sublinks zu den Stellenanzeigen in einer Liste. 
Danach Loopt das Skript durch diese Liste und vergleicht die Bescheibungen der Stellenzeigen mit vorgegebenen Keywords. Am Ende werden dann die gesamten Übereinstimmenden Schlagwörter jeder Beschreibung in einer Liste gespeichert und die einzigartige Menge dieser zu einer finalen Liste hinzugefügt. 

Am Ende werden dann die Vorkomnisse eines jeden Keywords in einem Barchart dargestellt. 

**Hier ein Auszug der 24 relevantesten Kentnisse aus 450 Stellenanzeigen:**  

![a]()



Disclaimer:
Das Scrapen von Stellenzeigen verstöß gegen die AGB von Indeed. Ich will hier nur zeigen wie das theoretisch möglich wäre und niemanden zu ähnlichen Handlungen verleiten. 

