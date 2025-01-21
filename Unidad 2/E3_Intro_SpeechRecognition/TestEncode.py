
cadena = 'results {\n  alternatives {\n    transcript: "clase de rob\\303\\263tica"\n    confidence: 0.7651427\n  }\n  result_end_time {\n    seconds: 1\n    nanos: 740000000\n  }\n  language_code: "es-us"\n}\ntotal_billed_time {\n  seconds: 2\n}\nrequest_id: 1928042458078544713\n'
#print(cadena)
#print(cadena.encode("latin-1").decode("utf8"))

#cad = "clase de rob\303\263tica"
#cad = cad.encode("latin-1")
#print(cad)
#print(cad.decode("utf8"))


cad = "str(\"clase de rob\\303\\263tica\")"
cad = eval(cad)
print(cad)
cad = cad.encode("latin-1")
print(cad.decode("utf8"))

