
# Matches municipality code for city/country (post 2010 data) to municipality code for country
# (pre-2010 data) and country name. Note: I'm writing in a dictionary for now just to keep track, but we can easily
# switch this to a function since the dictionary will obviously occupy space.
# Key is code for municipality in post-2010 data
# Value is a 2-tuple containing (<code for country in pre-2010 data>, <Name of Country in pre-2010 data>)

#Dev note - I started with the 2010 dataset (but switching to 2018) for the keys and using the 1998 (or later if not found) dataset for the values
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
    29351 : (11240, "ESPANHA"),

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
    
    
    29793 : (29025, “HONG KONG”),

    29661 : (29033, “IRLANDA”),

    29742 : (11380, "JAPÃO"),
    30139 : (11380, "JAPÃO"),
    30198 : (11380, "JAPÃO"),
    30236 : (11380, "JAPÃO"),
    30554 : (11380, "JAPÃO"),
    30589 : (11380, "JAPÃO"),
    30643 : (11380, "JAPÃO"),
    30627 : (11380, "JAPÃO"),
    30724 : (11380, "JAPÃO"),

    30082 : (98442, "FILIPINAS"),

    30147 : (11568, "URUGUAI"),

    30430 : (11568, "URUGUAI"),

    11568 : (11568, "URUGUAI"),

    29955 : (11509, "PORTUGAL"),

    98540 : (98540, "CHINA"),

    30481 : (11169, "CHILE"),

    30767 : (98949, "AUSTRIA"),

    30600 : (29076, "HONDURAS"),

    30350 : (98566, "CHECOSLOVÁQUIA"),

    29696 : (11100, "ALEMANHA"),

    30180 : (11100, "ALEMANHA"),

    29890 : (29130, "MALASIA"),

    29971 : (98841, "INGLATERRA"),

    30163 : (98760, "RUSSIA"),

    29432 : (98922, "BELGICA"),

    29092 : (29092, "ZIMBABWE"),

    30104 : (11428, "MEXICO"),

    30279 : (11541, "SURINAME"),

    29505 : (11584, "VENEZUELA"),

    29564 : (11584, "VENEZUELA"),

    11800 : (11800, "BOLIVIA"),

    29572 : (11800, "BOLIVIA"),

    29904 : (11800, "BOLIVIA"),

    30473 : (11800, "BOLIVIA"),

    29599 : (98485, "DINAMARCA"),

    30260 : (98329, "PANAMA"),

    30821 : (29068, "NAMIBIA"),

    29912 : (98361, "NIGERIA"),

    98361 : (98361, "NIGERIA"),

    29556 : (11444, "PARAGUAI"),

    29580 : (11444, "PARAGUAI"),

    29670 : (11444, "PARAGUAI"),

    30309 : (11444, "PARAGUAI"),

    30465 : (11444, "PARAGUAI"),

    30155 : (98906, "CANADA"),

    30252 : (98906, "CANADA"),

    30635 : (98906, "CANADA"),

    39063 : (98906, "CANADA"),

    29882 : (29157, "KUWAIT"),

    30325 : (98140, "TRINIDAD TOBAGO"),

    29424 : (98663, "BARBADOS"),

    29440 : (98647, "ROMENIA"),

    29459 : (29238, "HUNGRIA"),

    29467 : (11142, "ARGENTINA"),

    29475 : (11320, "GUIANA FRANCESA"),

    29483 : (98086, "EGITO"),

    29491 : (98981, "AUSTRALIA"),

    29513 : (11266, "ESTADOS UNIDOS"),

    29530 : (98787, "AFRICA DO SUL"),

    29548 : (98523, "CINGAPURA"),

    29580 : (98485, "DINAMARCA"),

    29602 : (11142, "ARGENTINA"),

    29610 : (98248, "SENEGAL"),

    29637 : (98221, "SIRIA"),

    29688 : (98744, "SUECIA"),

    98043 : (98043, "GANA"),

    29700 : (11525, "SUICA"),

    29718 : (11304, "GUIANA"),

    29726 : (98000, "GUATEMALA"),

    29246 : (29246, "HAITI"),

    29750 : (2800, "VIETNA"),

    30902 : (11266, "ESTADOS UNIDOS"),

    29777 : (98868, "CUBA"),

    29785 : (98426, "FINLANDIA"),

    29807 : (11266, "ESTADOS UNIDOS"),

    29840 : (29211, "INDONESIA"),

    29866 : (29190, "JAMAICA"),

    29939 : (98060, "GABAO"),

    29947 : (11460, "PERU"),

    29980 : (11266, "ESTADOS UNIDOS"),

    29998 : (98965, "ANGOLA"),

    30066 : (11240, "ESPANHA"),

    30074 : (98838, "NICARAGUA"),

    30090 : (29116, "MOCAMBIQUE"),

    39004 : (11142, "ARGENTINA"),

    30112 : (11266, "ESTADOS UNIDOS"),

    30120 : (11363, "ITALIA"),

    30171 : (98825, "INDIA"),

    30201 : (29165, "KENIA"),

    30210 : (98825, "INDIA"),

    30228 : (11266, "ESTADOS UNIDOS"),

    30244 : (98345, "NORUEGA"),

    98302 : (98302, "PAQUISTAO"),

    30287 : (11282, "FRANCA"),

    30317 : (98540, "CHINA"),

    11460 : (11460, "PERU"),

    30341 : (11509, "PORTUGAL"),

    30368 : (98604, "CABO VERDE"),

    30376 : (98787, "AFRICA DO SUL"),

    30392 : (11223, "EQUADOR"),

    30406 : (29122, "MARROCOS"),

    30422 : (11126, "ARABIA SAUDITA"),

    30449 : (11363, "ITALIA"),

    30457 : (29009, "PAISES BAIXOS"),

    30538 : (11207, "COREIA"),

    30562 : (98981, "AUSTRALIA"),

    30490 : (98280, "REPUBLICA DOMINICANA"),

    30503 : (11266, "ESTADOS UNIDOS"),

    30511 : (98507, "COSTA RICA"),

    30520 : (98469, "EL SALVADOR"),

    30546 : (98620, "BULGARIA"),

    30570 : (2828, "TAIWAN"),

    30597 : (29203, "IRA"),

    30619 : (11347, "ISRAEL"),

    30686 : (29149, "LIBIA"),

    30708 : (98124, "TUNISIA"),

    11762 : (11762, "UCRANIA"),

    30740 : (11487, "POLONIA"),

    30783 : (11266, "ESTADOS UNIDOS"),

    30805 : (29050, "NOVA ZELANDIA"),

    30848 : (98540, "CHINA"),

    29092 : (29092, "ZIMBABWE"),

    #Note, this was beginning in the 2010 electorate dataset, but planning to start again in 2018
    30864 : (11525, "SUICA")

}







}
