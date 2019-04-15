--
-- File generated with SQLiteStudio v3.2.1 on Sen Apr 15 11:18:55 2019
--
-- Text encoding used: UTF-8
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: DimensiSoalHexaco
CREATE TABLE DimensiSoalHexaco (idDimensi INTEGER PRIMARY KEY AUTOINCREMENT, Dimensi TEXT NOT NULL);
INSERT INTO DimensiSoalHexaco (idDimensi, Dimensi) VALUES (1, 'Sincerity');
INSERT INTO DimensiSoalHexaco (idDimensi, Dimensi) VALUES (2, 'Fairnes');
INSERT INTO DimensiSoalHexaco (idDimensi, Dimensi) VALUES (3, 'Greed Avoidance');
INSERT INTO DimensiSoalHexaco (idDimensi, Dimensi) VALUES (4, 'Modesty');
INSERT INTO DimensiSoalHexaco (idDimensi, Dimensi) VALUES (5, 'Fearfulness');
INSERT INTO DimensiSoalHexaco (idDimensi, Dimensi) VALUES (6, 'Anxiety');
INSERT INTO DimensiSoalHexaco (idDimensi, Dimensi) VALUES (7, 'Dependence');
INSERT INTO DimensiSoalHexaco (idDimensi, Dimensi) VALUES (8, 'Sentimentality');
INSERT INTO DimensiSoalHexaco (idDimensi, Dimensi) VALUES (9, 'Social Self-Estimate');
INSERT INTO DimensiSoalHexaco (idDimensi, Dimensi) VALUES (10, 'Social Boldness');
INSERT INTO DimensiSoalHexaco (idDimensi, Dimensi) VALUES (11, 'Socialbility');
INSERT INTO DimensiSoalHexaco (idDimensi, Dimensi) VALUES (12, 'Liveliness');
INSERT INTO DimensiSoalHexaco (idDimensi, Dimensi) VALUES (13, 'Forgiveness');
INSERT INTO DimensiSoalHexaco (idDimensi, Dimensi) VALUES (14, 'Gentleness');
INSERT INTO DimensiSoalHexaco (idDimensi, Dimensi) VALUES (15, 'Flexibility');
INSERT INTO DimensiSoalHexaco (idDimensi, Dimensi) VALUES (16, 'Patience');
INSERT INTO DimensiSoalHexaco (idDimensi, Dimensi) VALUES (17, 'Organizations');
INSERT INTO DimensiSoalHexaco (idDimensi, Dimensi) VALUES (18, 'Dilligence');
INSERT INTO DimensiSoalHexaco (idDimensi, Dimensi) VALUES (19, 'Perfectionism');
INSERT INTO DimensiSoalHexaco (idDimensi, Dimensi) VALUES (20, 'Prudence');
INSERT INTO DimensiSoalHexaco (idDimensi, Dimensi) VALUES (21, 'Aesthetic Appreciation');
INSERT INTO DimensiSoalHexaco (idDimensi, Dimensi) VALUES (22, 'Inquitiviness');
INSERT INTO DimensiSoalHexaco (idDimensi, Dimensi) VALUES (23, 'Creativity');
INSERT INTO DimensiSoalHexaco (idDimensi, Dimensi) VALUES (24, 'Unconventionality');
INSERT INTO DimensiSoalHexaco (idDimensi, Dimensi) VALUES (25, 'Alturism');

-- Table: InputPeserta
CREATE TABLE InputPeserta (idinputpeserta INTEGER PRIMARY KEY AUTOINCREMENT, idpeserta INT REFERENCES "Rincian Data Peserta" (idpeserta) ON DELETE SET NULL);

-- Table: Rincian Data Peserta
CREATE TABLE "Rincian Data Peserta" (idpeserta INTEGER NOT NULL, idtipesoal INTEGER, "No Tes" INT, "Tanggal Tes" DATE, "Nama Kandidat" TEXT, "Jenis Kelamin" TEXT, "Tanggal Lahir" DATE, "Pendidikan Terakhir" TEXT, "Jurusan Pendidikan" TEXT, Kota TEXT, "Perusahaan / Instansi" TEXT, "Posisi / Jabatan" TEXT);
INSERT INTO "Rincian Data Peserta" (idpeserta, idtipesoal, "No Tes", "Tanggal Tes", "Nama Kandidat", "Jenis Kelamin", "Tanggal Lahir", "Pendidikan Terakhir", "Jurusan Pendidikan", Kota, "Perusahaan / Instansi", "Posisi / Jabatan") VALUES (1, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);

-- Table: TipeSoal
CREATE TABLE TipeSoal (idTipeSoal INTEGER PRIMARY KEY ON CONFLICT ROLLBACK AUTOINCREMENT, NamaSoal TEXT);
INSERT INTO TipeSoal (idTipeSoal, NamaSoal) VALUES (1, 'tipe 60');
INSERT INTO TipeSoal (idTipeSoal, NamaSoal) VALUES (2, 'tipe 80');
INSERT INTO TipeSoal (idTipeSoal, NamaSoal) VALUES (3, 'tipe 100');

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
