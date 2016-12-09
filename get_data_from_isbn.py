import requests
import json

#r = requests.get("http://isbndb.com/api/v2/json/NAZ4ZQZO/book/9780849303159")
#text = r.text

#note r added before result string

#text = r (return here where it shouldn't be if you want to run test case)
"""{
   "index_searched" : "isbn",
   "data" : [
      {
         "language" : "eng",
         "title_latin" : "Principles of solid mechanics",
         "publisher_id" : "crc_press",
         "publisher_name" : "CRC Press",
         "urls_text" : "",
         "publisher_text" : "Boca Raton, FL : CRC Press, 2000.",
         "physical_description_text" : "446 p. : ill. ; 24 cm.",
         "summary" : "Evolving from more than 30 years of research and teaching experience, \"Principles of Solid Mechanics\" offers an in-depth treatment of the application of the full-range theory of deformable solids for analysis and design. Unlike other texts, it is not either a civil or mechanical engineering text, but both. It treats not only analysis but incorporates design along with experimental observation. Principles of Solid Mechanics serves as a core course textbook for advanced seniors and first-year graduate students. The author focuses on basic concepts and applications, simple yet unsolved problems, inverse strategies for optimum design, unanswered questions, and unresolved paradoxes to intrigue students and encourage further study. He includes plastic as well as elastic behavior in terms of a unified field theory and discusses the properties of field equations and requirements on boundary conditions crucial for understanding the limits of numerical modeling. Designed to help guide students with little experimental experience and no exposure to drawing and graphic analysis, the text presents carefully selected worked examples. The author makes liberal use of footnotes and includes over 150 figures and 200 problems. This, along with his approach, allows students to see the full range, non-linear response of structures.",
         "author_data" : [
            {
               "name" : "Richards, Rowland",
               "id" : "richards_rowland"
            }
         ],
         "title_long" : "",
         "subject_ids" : [
            "mechanics_applied"
         ],
         "isbn13" : "9780849303159",
         "awards_text" : "",
         "book_id" : "principles_of_solid_mechanics",
         "notes" : "Includes bibliographical references and index.\n\n1. Introduction -- 2. Strain and stress -- 3. Stress-strain relationships (rheology) -- 4. Strategies for elastic analysis and design -- 5. Linear free fields -- 6. Two-dimensional solutions for straight and circular beams -- 7. Ring, holes, and inverse problems -- 8. Wedges and half-space -- 9. Torsion -- 10. Concepts of plasticity -- 11. One-dimensional plasticity for design -- 12. Slip-line analysis.",
         "marc_enc_level" : "",
         "dewey_normal" : "620.105",
         "isbn10" : "084930315X",
         "title" : "Principles of solid mechanics",
         "lcc_number" : "TA350",
         "dewey_decimal" : "620/.1/05",
         "edition_info" : "(alk. paper)"
      }
   ]
}"""


def get_info(isbn):
    #isbn inputted as string
    address = "http://isbndb.com/api/v2/json/NAZ4ZQZO/book/"+isbn
    r = requests.get(address)
    data = json.loads(r.text)
    info_to_return = {}
    given_info = data.get("data")[0]
    info_to_return["author"] = given_info.get("author_data")[0].get("name")
    info_to_return["title"] = given_info.get("title_latin")
    return (info_to_return)













