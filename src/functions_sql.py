import sqlalchemy as alch
from sqlalchemy.exc import SQLAlchemyError

class Motor_db:
    
    def __init__(self, name, password):

        # nuestra clase va a recibir dos parámetros que son fijos a lo largo de toda la BBDD, el nombre de la BBDD y la contraseña con el servidor. 
        self.name = name
        self.password = password

    def create_db(self):

        engine = alch.create_engine(f"mysql+pymysql://root:{self.password}@localhost")
        try:
            engine.execute(f"CREATE DATABASE {self.name} DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_bin;")
            print(f"---------- '{self.name}' ha sido creada con éxito ----------")
        except:
            print("ERROR:  La BBDD ya existe")


    def conexion_db(self):
        return alch.create_engine(f"mysql+pymysql://root:{self.password}@localhost/{self.name}")


    def create_table(self, query):
        engine = self.conexion_db()
        try:
            engine.execute(query)
            
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            return error
        
    def sacar_id(self, link, col_id,  column, table):

        engine = self.conexion_db()

        try:
            query_sacar_id = f"SELECT {col_id} FROM {table} WHERE {column} = '{link}'"

            id_ = engine.execute(query_sacar_id).first()

            if not id_:
                return "Ese id no esta en la BBDD"
            else:
                return engine.execute(query_sacar_id).first()[0]

        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            return error

def createtables_bbdd():
    tables = {'table_type' : """
    CREATE TABLE IF NOT EXISTS `estate_db`.`type` (
    `idtype` VARCHAR(45) NOT NULL,
    PRIMARY KEY (`idtype`))
    ENGINE = InnoDB;
    """,

    'table_region' : """
    CREATE TABLE IF NOT EXISTS `estate_db`.`region` (
    `idregion` VARCHAR(45) NOT NULL,
    PRIMARY KEY (`idregion`))
    ENGINE = InnoDB;
    """,

    'table_province' : """
    CREATE TABLE IF NOT EXISTS `estate_db`.`province` (
    `idprovince` VARCHAR(100) NOT NULL,
    PRIMARY KEY (`idprovince`))
    ENGINE = InnoDB;
    """,

    'table_zipcode' : """
    CREATE TABLE IF NOT EXISTS `estate_db`.`zipcode` (
    `idzipcode` VARCHAR(5) NOT NULL,
    PRIMARY KEY (`idzipcode`))
    ENGINE = InnoDB;
    """,

    'table_city' : """
    CREATE TABLE IF NOT EXISTS `estate_db`.`city` (
    `idcity` VARCHAR(100) NOT NULL,
    PRIMARY KEY (`idcity`))
    ENGINE = InnoDB;
    """,

    'table_coordinates' : """
    CREATE TABLE IF NOT EXISTS `estate_db`.`coordinates` (
    `idcoordinates` INT NOT NULL AUTO_INCREMENT,
    `latitude` FLOAT NOT NULL,
    `longitude` FLOAT NOT NULL,
    `idregion` VARCHAR(45) NOT NULL,
    `idprovince` VARCHAR(100) NOT NULL,
    `idzipcode` VARCHAR(5) NOT NULL,
    `idcity` VARCHAR(100) NOT NULL,
    PRIMARY KEY (`idcoordinates`),
    INDEX `fk_coordinates_region1_idx` (`idregion` ASC) VISIBLE,
    INDEX `fk_coordinates_province1_idx` (`idprovince` ASC) VISIBLE,
    INDEX `fk_coordinates_zipcode1_idx` (`idzipcode` ASC) VISIBLE,
    INDEX `fk_coordinates_city1_idx` (`idcity` ASC) VISIBLE,
    CONSTRAINT `fk_coordinates_region1`
        FOREIGN KEY (`idregion`)
        REFERENCES `estate_db`.`region` (`idregion`)
        ON DELETE NO ACTION
        ON UPDATE NO ACTION,
    CONSTRAINT `fk_coordinates_province1`
        FOREIGN KEY (`idprovince`)
        REFERENCES `estate_db`.`province` (`idprovince`)
        ON DELETE NO ACTION
        ON UPDATE NO ACTION,
    CONSTRAINT `fk_coordinates_zipcode1`
        FOREIGN KEY (`idzipcode`)
        REFERENCES `estate_db`.`zipcode` (`idzipcode`)
        ON DELETE NO ACTION
        ON UPDATE NO ACTION,
    CONSTRAINT `fk_coordinates_city1`
        FOREIGN KEY (`idcity`)
        REFERENCES `estate_db`.`city` (`idcity`)
        ON DELETE NO ACTION
        ON UPDATE NO ACTION)
    ENGINE = InnoDB;
    """,

    'table_features' : """
    CREATE TABLE IF NOT EXISTS `estate_db`.`feautures` (
    `idFeautures` INT NOT NULL AUTO_INCREMENT,
    `id_vivienda` VARCHAR(45) NOT NULL,
    `date` DATE NOT NULL,
    `advertiser` VARCHAR(45) NULL,
    `descriptions` VARCHAR(45) NULL,
    `rooms` INT NOT NULL,
    `bathrooms` INT NOT NULL,
    `surface` INT NOT NULL,
    `energy_certificate` INT NOT NULL,
    `antiquity` INT NOT NULL,
    `floor` INT NOT NULL,
    `surfaceland` INT NOT NULL,
    `price` INT NOT NULL,
    `idtype` VARCHAR(45) NOT NULL,
    `idcoordinates` INT NOT NULL,
    PRIMARY KEY (`idFeautures`),
    INDEX `fk_Feautures_type_idx` (`idtype` ASC) VISIBLE,
    INDEX `fk_Feautures_coordinates1_idx` (`idcoordinates` ASC) VISIBLE,
    CONSTRAINT `fk_Feautures_type`
        FOREIGN KEY (`idtype`)
        REFERENCES `estate_db`.`type` (`idtype`)
        ON DELETE NO ACTION
        ON UPDATE NO ACTION,
    CONSTRAINT `fk_Feautures_coordinates1`
        FOREIGN KEY (`idcoordinates`)
        REFERENCES `estate_db`.`coordinates` (`idcoordinates`)
        ON DELETE NO ACTION
        ON UPDATE NO ACTION)
    ENGINE = InnoDB;
    """}
    for k in tables.keys():
        realestate.create_table(tables[k])
        print(k)

def insert_datacol():
    '''
    Función que nos permite insertar datos en la BBDD, concretamente en tablas que solo tengan una unica columna.
    Argumentos:
        key: name column dataframe
        value[0]: name table db
        value[1]: name column table db
    '''
    dicc_tables = {'region': ['region', 'idregion'], 
                'province': ['province', 'idprovince'], 
                'city': ['city', 'idcity'], 
                'zipcode': ['zipcode', 'idzipcode'],
                'subtypeId': ['type', 'idtype']}

    key_list = [k for k in dicc_tables.keys()]

    for key in key_list:
        for item in df[key].unique():

            query= f"""INSERT INTO {dicc_tables[key][0]} ({dicc_tables[key][1]}) 
                        VALUES ("{item}");"""

            id_bd = realestate.sacar_id( f'{item}', f"{dicc_tables[key][1]}" , f"{dicc_tables[key][1]}", f"{dicc_tables[key][0]}")

            if id_bd == 'Ese id no esta en la BBDD' : 
                realestate.create_table(query)

            else:
                pass

def insert_coordinates():
    '''
    Función que nos permite insertar datos en la BBDD, concretamente en la tabla coordinates.
    '''

    for index, row in df.iterrows():
        
        id_region = realestate.sacar_id(f"{row['region']}", "idregion" , "idregion", "region")    
        id_province = realestate.sacar_id(f"{row['province']}", "idprovince" , "idprovince", "province")
        id_city = realestate.sacar_id(f"{row['city']}", "idcity" , "idcity", "city")
        id_zipcode = realestate.sacar_id(f"{row['zipcode']}", "idzipcode" , "idzipcode", "zipcode")
        
        
        query_medidas = f"""INSERT INTO coordinates (latitude, longitude, idregion, idprovince, idzipcode, idcity)
                    VALUES ({row['latitude']}, {row['longitude']}, {id_region}, {id_province}, {id_zipcode}, {id_city});"""
        
        realestate.create_table(query_medidas)

def insert_features():
    '''
    Función que nos permite insertar datos en la BBDD, concretamente en la tabla features.
    '''

    for index, row in df.iterrows():
        
        id_coordinates = realestate.sacar_id(f"{row['latitude']}", "idcoordinates" , "idcoordinates", "coordinates")
        id_type = realestate.sacar_id(f"{row['subtypeId']}", "idtype" , "idtype", "type")
        
        
        query_medidas = f"""INSERT INTO coordinates (id_vivienda, date, advertiser, descriptions, rooms, bathrooms, surface, energy_certificate, antiquity, floor, surfaceland, price, idtype, idcoordinates)
                    VALUES ({row['id']}, {row['date']}, {row['advertiser']}, {row['descriptions']}, {row['rooms']}, {row['bathrooms']}, {row['surface']}, {row['energy_certificate']}, {row['antiquity']}, {row['floor']}, {row['surfaceland']}, {row['price']}, {id_type}, {id_coordinates});"""
        
        realestate.create_table(query_medidas)
