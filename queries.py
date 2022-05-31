features_laptops = ["BrandName", "ModelName", "Processor", "RAM", "OperatingSystem", 
                    "Memory", "Display", "OriginalPrice", "Discount", "OfferPrice"]

create_table_query = '''
        CREATE TABLE IF NOT EXISTS LAPTOPS 
        (
        {} TEXT NOT NULL, {} TEXT NOT NULL, {} TEXT, 
        {} TEXT, {} TEXT, {} TEXT, {} TEXT, 
        {} INTEGER, {} INTEGER, {} INTEGER
        )
        '''.format(features_laptops[0], features_laptops[1], features_laptops[2], features_laptops[3], features_laptops[4],
                   features_laptops[5], features_laptops[6], features_laptops[7], features_laptops[8], features_laptops[9])

insert_query = '''
        INSERT INTO LAPTOPS ({}, {}, {}, {}, {}, {}, {}, {}, {}, {})
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        '''.format(features_laptops[0], features_laptops[1], features_laptops[2], features_laptops[3], features_laptops[4],
                   features_laptops[5], features_laptops[6], features_laptops[7], features_laptops[8], features_laptops[9])