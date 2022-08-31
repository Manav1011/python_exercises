import psutil
  
# check if chrome is open
"chrome.exe" in (i.name() for i in psutil.process_iter())