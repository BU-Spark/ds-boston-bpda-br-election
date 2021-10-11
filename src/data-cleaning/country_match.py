
# Matches municipality code for city/country (post 2010 data) to municipality code for country
# (pre-2010 data) and country name. Note: I'm writing in a dictionary for now just to keep track, but we can easily
# switch this to a function since the dictionary will obviously occupy space.
# Key is code for municipality in post-2010 data
# Value is a 2-tuple containing (<code for country in pre-2010 data>, <Name of Country in pre-2010 data>)

#Dev note - I'm starting in the 2010 dataset for the keys and using the 1998 (or later if not found) dataset for the values
country_code_map = {

    #Maps code for ABIDJAN-COTE (Abidjan Cote de'Ivoire)
    29254 : (98582, "COSTA DO MARFIM"), 

    #Maps code for ABU DHABI-EAU (Abu Dhabi, UAE)
    29262 : (98728, "EMIRADOS ARABES"),

    #Maps code for AMÃ-JORD (Amman, Jordan)
    29289 : (29181, "JORDANIA"),

    #Maps code for ANCARA-TURQ (Ankara, Turkey)
    29297 : (98108, "TURQUIA"),

    #Maps code for ARGEL-ARGL (Algiers, Algeria)
    29300 : (98701, "ARGELIA"),

    #Maps code for  ARGENTINA (Argentina) - This is really a no-op as there is no change here
    11142 : (11142, "ARGENTINA"),

    #Maps code for ASSUNÇÃO-PARG (Asuncion, Paraguay)
    29327 : (11444, "PARAGUAI"),

    #Maps code for ASTANA-KAZA (Astana, Kazakhstan)
    #Note: there is no prior country code for kazakhstan, so leaving as is
    39241 : (39241, "ASTANA-KAZA"),

    #Maps code for ATENAS-GREC (Athens, Greece)
    29335 : (11827, "GRECIA"),

    #Maps code for ATLANTA-EUA (Atlanta, USA)
    39080 : (11266, "ESTADOS UNIDOS"),

    #Maps code for BANGKOK-TAIL (Bangkok, Thailand)
    29343 : (98205, "TAILANDIA"),

    #Maps code for BARCELONA-ESPA (Barcelona, Spain)
    29343 : (11240, "ESPANHA"),

    #Maps code for  BEIRUTE-LBAN (Beirut, Lebanon)
    29360 : (11401, "LIBANO"),

    #Maps code for  BELGRADO-SERV (Belgrade, Serbia)
    # Note: this would have been included in IUGUSLÁVIA (code 29173), we can change to that or keep as is
    # For now, keeping as no-op
    29378 : (29378, "BELGRADO-SERV"),

    #Maps code for  BERLIM-RFA (Berlin, Germany)
    29386 : (11100, "ALEMANHA"),

    #Maps code for  BISSAU-GUIB (Guinea-Bissau)
    29394 : (98027, "GUINE BISSAU"),

    #Maps code for  BOGOTÁ-COLO (Bogota, Colombia)
    29408 : (11185, "COLOMBIA"),

    #Maps code for  BOLÍVIA (Bolivia) - This is another no-op (no change)
    11800 : (11800, "BOLIVIA"),

    #Maps code for  BOSTON-EUA (Boston, USA)
    29416 : (11266, "ESTADOS UNIDOS"),

    #Take over here at row 1380 of 2010 electorate dataset 







}