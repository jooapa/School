using System;
using System.Collections;
using System.Collections.Generic;
using System.Data.SqlClient;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.ComponentModel.Design.ObjectSelectorEditor;
using static System.Net.Mime.MediaTypeNames;
using System.Windows.Forms;
using System.Diagnostics;



namespace Autokauppa.model
{
    public class DatabaseHallinta
    {
        string yhteysTiedot;
        private SqlConnection dbYhteys;
        private SqlDataReader reader;

        public DatabaseHallinta()
        {
            yhteysTiedot =
             "Server=(localdb)\\MSSQLLocalDB;" +
             "Database=Autokoulu;" +
             "Trusted_Connection=True;";
        }

        public bool ConnectDatabase()
        {
            dbYhteys = new SqlConnection(yhteysTiedot);
            try
            {
                dbYhteys.Open();
                return true;
            }
            catch (Exception)
            {
                return false;
            }
        }

        public void DisconnectDatabase()
        {
            dbYhteys.Close();
        }

        public bool SaveAutoIntoDatabase(Auto newAuto)
        {
            bool palaute = false;
            return palaute;
        }

        public Auto GetAutoFromDatabase(int id)
        {
            ConnectDatabase();
            string query = "";
            //string query = @"SELECT * FROM auto
            //                ORDER BY(SELECT NULL)
            //                OFFSET " + id + @" ROWS
            //                FETCH NEXT 1 ROWS ONLY;"
            //string query = @"SELECT * FROM auto
            //                ORDER BY hinta ASC
            //                OFFSET " + id + @" ROWS
            //                FETCH NEXT 1 ROWS ONLY;";
            query = @"SELECT * FROM auto
                        ORDER BY hinta ASC
                        OFFSET " + id + @" ROWS
                        FETCH NEXT 1 ROWS ONLY;";


            SqlCommand command = new(query, dbYhteys);
            reader = command.ExecuteReader();
            Auto auto = new();
            while (reader.Read())
            {
                auto.ID = reader.GetInt32(0);
                auto.Hinta = reader.GetDecimal(1);
                auto.Rekisteri_paivamaara = reader.GetDateTime(2);
                auto.Moottorin_tilavuus = reader.GetDecimal(3);
                auto.Mittarilukema = reader.GetInt32(4);
                auto.AutonMerkkiID = reader.GetInt32(5);
                auto.AutonMalliID = reader.GetInt32(6);
                auto.VaritID = reader.GetInt32(7);
                auto.PolttoaineID = reader.GetInt32(8);
            }
            DisconnectDatabase();
            return auto;
        }

        internal string GetAutonMalli(int id)
        {
            ConnectDatabase();
            string query = @"SELECT * FROM autonmallit
                            WHERE ID = " + id + ";";
            SqlCommand command = new(query, dbYhteys);
            reader = command.ExecuteReader();
            string malli = "";
            while (reader.Read())
            {
                malli = reader.GetString(1);
            }
            DisconnectDatabase();
            return malli;
        }

        internal string GetAutonMerkki(int id)
        {
            ConnectDatabase();
            string query = @"SELECT * FROM AutonMerkki
                            WHERE ID = " + id + ";";
            SqlCommand command = new(query, dbYhteys);
            reader = command.ExecuteReader();
            string malli = "";
            while (reader.Read())
            {
                malli = reader.GetString(1);
            }
            DisconnectDatabase();
            return malli;
        }

        internal string GetPolttoaine(int id)
        {
            ConnectDatabase();
            string query = @"SELECT * FROM Polttoaine
                            WHERE ID = " + id + ";";
            SqlCommand command = new(query, dbYhteys);
            reader = command.ExecuteReader();
            string malli = "";
            while (reader.Read())
            {
                malli = reader.GetString(1);
            }
            DisconnectDatabase();
            return malli;
        }

        internal string GetVari(int id)
        {
            ConnectDatabase();
            string query = @"SELECT * FROM Varit
                            WHERE ID = " + id + ";";
            SqlCommand command = new(query, dbYhteys);
            reader = command.ExecuteReader();
            string malli = "";
            while (reader.Read())
            {
                malli = reader.GetString(1);
            }
            DisconnectDatabase();
            return malli;
        }
        internal List<AutonMallit> GetAutonMallit()
        {
            ConnectDatabase();
            string query = @"SELECT * FROM autonmallit;";
            SqlCommand command = new(query, dbYhteys);
            reader = command.ExecuteReader();
            List<AutonMallit> mallit = new();
            while (reader.Read())
            {
                AutonMallit malli = new()
                {
                    ID = reader.GetInt32(0),
                    AutonMalli = reader.GetString(1),
                    AutonMerkkiID = reader.GetInt32(2)
                };
                mallit.Add(malli);
            }
            DisconnectDatabase();
            return mallit;
        }

        internal List<AutonMerkki> GetAutonMerkit()
        {
            ConnectDatabase();
            string query = @"SELECT * FROM AutonMerkki;";
            SqlCommand command = new(query, dbYhteys);
            reader = command.ExecuteReader();
            List<AutonMerkki> merkit = new();
            while (reader.Read())
            {
                AutonMerkki merkki = new()
                {
                    ID = reader.GetInt32(0),
                    Merkki = reader.GetString(1)
                };
                merkit.Add(merkki);
            }
            DisconnectDatabase();
            return merkit;
        }

        internal List<Polttoaine> GetPolttoaineet()
        {

            ConnectDatabase();
            string query = @"SELECT * FROM Polttoaine;";
            SqlCommand command = new(query, dbYhteys);
            reader = command.ExecuteReader();
            List<Polttoaine> polttoaineet = new();
            while (reader.Read())
            {
                Polttoaine polttoaine = new()
                {
                    ID = reader.GetInt32(0),
                    PolttoaineNimi = reader.GetString(1)
                };
                polttoaineet.Add(polttoaine);
            }
            DisconnectDatabase();
            return polttoaineet;
        }
        internal List<Varit> GetVarit()
        {
            ConnectDatabase();
            string query = @"SELECT * FROM Varit;";
            SqlCommand command = new(query, dbYhteys);
            reader = command.ExecuteReader();
            List<Varit> varit = new();
            while (reader.Read())
            {
                Varit vari = new()
                {
                    ID = reader.GetInt32(0),
                    Vari = reader.GetString(1)
                };
                varit.Add(vari);
            }
            DisconnectDatabase();
            return varit;
        }

        internal int GetLength()
        {
            ConnectDatabase();
            string query = "SELECT COUNT(*) FROM auto;";
            SqlCommand command = new(query, dbYhteys);
            reader = command.ExecuteReader();
            int length = 0;
            while (reader.Read())
            {
                length = reader.GetInt32(0);
            }
            DisconnectDatabase();
            return length;
        }

        internal int GetAutoHintaLastID()
        {
            ConnectDatabase();
            // SELECT MAX(Hinta) FROM auto; but we need the ID
            string query = "SELECT TOP 1 * FROM auto ORDER BY ID DESC;";
            SqlCommand command = new(query, dbYhteys);
            reader = command.ExecuteReader();
            int autoID = 0;
            while (reader.Read())
            {
                autoID = reader.GetInt32(0);
            }
            DisconnectDatabase();
            return autoID;
        }

        internal int GetAutoHintaFirstID()
        {
            ConnectDatabase();
            string query = "SELECT TOP 1 * FROM auto ORDER BY ID ASC;";
            SqlCommand command = new(query, dbYhteys);
            reader = command.ExecuteReader();
            int autoID = 0;
            while (reader.Read())
            {
                autoID = reader.GetInt32(0);
            }
            DisconnectDatabase();
            return autoID;
        }

        internal int GetAutonMalliIDFromText(string text)
        {
            ConnectDatabase();
            string query = @"SELECT * FROM autonmallit
                            WHERE Auton_mallin_nimi = '" + text + "';";
            SqlCommand command = new(query, dbYhteys);
            reader = command.ExecuteReader();
            int malliID = 0;
            while (reader.Read())
            {
                malliID = reader.GetInt32(0);
            }
            DisconnectDatabase();
            return malliID;
        }

        internal int GetAutonMerkkiIDFromText(string text)
        {
            ConnectDatabase();
            string query = @"SELECT * FROM AutonMerkki
                            WHERE Merkki = '" + text + "';";
            SqlCommand command = new(query, dbYhteys);
            reader = command.ExecuteReader();
            int merkkiID = 0;
            while (reader.Read())
            {
                merkkiID = reader.GetInt32(0);
            }
            DisconnectDatabase();
            return merkkiID;
        }

        internal int GetPolttoaineIDFromText(string text)
        {
            ConnectDatabase();
            string query = @"SELECT * FROM Polttoaine
                            WHERE Polttoaineen_nimi = '" + text + "';";
            SqlCommand command = new(query, dbYhteys);
            reader = command.ExecuteReader();
            int polttoaineID = 0;
            while (reader.Read())
            {
                polttoaineID = reader.GetInt32(0);
            }
            DisconnectDatabase();
            return polttoaineID;
        }

        internal int GetVariIDFromText(string text)
        {
            ConnectDatabase();
            string query = @"SELECT * FROM Varit
                            WHERE Varin_nimi = '" + text + "';";
            SqlCommand command = new(query, dbYhteys);
            reader = command.ExecuteReader();
            int variID = 0;
            while (reader.Read())
            {
                variID = reader.GetInt32(0);
            }
            DisconnectDatabase();
            return variID;
        }

        internal void UpdateAuto(Auto auto)
        {
            ConnectDatabase();
            string query = @"UPDATE auto
                            SET hinta = " + auto.Hinta + @",
                            rekisteri_paivamaara = '" + auto.Rekisteri_paivamaara + @"',
                            moottorin_tilavuus = " + auto.Moottorin_tilavuus + @",
                            mittarilukema = " + auto.Mittarilukema + @",
                            autonMerkkiID = " + auto.AutonMerkkiID + @",
                            autonMalliID = " + auto.AutonMalliID + @",
                            varitID = " + auto.VaritID + @",
                            polttoaineID = " + auto.PolttoaineID + @"
                            WHERE ID = " + auto.ID + @";";
            SqlCommand command = new(query, dbYhteys);
            reader = command.ExecuteReader();
            DisconnectDatabase();
        }

        internal int GetAutoCountID()
        {
            ConnectDatabase();
            string query = "select count(*) from auto";
            SqlCommand command = new(query, dbYhteys);
            reader = command.ExecuteReader();
            int count = 0;
            while (reader.Read())
            {
                count = reader.GetInt32(0);
            }
            DisconnectDatabase();
            return count;
        }

        internal void DeleteAuto(int id)
        {
            ConnectDatabase();
            string query = @"DELETE FROM auto
                            WHERE ID = " + id + @";";
            SqlCommand command = new(query, dbYhteys);
            reader = command.ExecuteReader();
            DisconnectDatabase();
        }
        public int GetNextAvailableAutoID()
        {
            ConnectDatabase();
            string query = "SELECT ID FROM auto ORDER BY ID ASC;";
            SqlCommand command = new(query, dbYhteys);
            reader = command.ExecuteReader();

            List<int> ids = new();
            while (reader.Read())
            {
                ids.Add(reader.GetInt32(0));
            }

            // Find the smallest missing ID
            int nextID = 1; // Start from 1 or any other minimum ID you want
            foreach (int id in ids)
            {
                if (id == nextID)
                {
                    nextID++;
                }
                else
                {
                    break;
                }
            }
            DisconnectDatabase();
            return nextID;
        }

        internal void AddNewAuto(Auto auto)
        {
            ConnectDatabase();
            //string query = @"INSERT INTO auto (Hinta, Rekisteri_paivamaara, Moottorin_tilavuus, Mittarilukema, AutonMerkkiID, AutonMalliID, VaritID, PolttoaineID)
            //        VALUES(
            //        " + auto.Hinta + @",
            //        '" + auto.Rekisteri_paivamaara + @"',
            //        -- from , -> . mottori tilavuudessa
            //        " + auto.Moottorin_tilavuus.ToString(System.Globalization.CultureInfo.InvariantCulture) + @",
            //        " + auto.Mittarilukema + @",
            //        " + auto.AutonMerkkiID + @",
            //        " + auto.AutonMalliID + @",
            //        " + auto.VaritID + @",
            //        " + auto.PolttoaineID + @");";
            string query = @"INSERT INTO auto (Hinta, Rekisteri_paivamaara, Moottorin_tilavuus, Mittarilukema, AutonMerkkiID, AutonMalliID, VaritID, PolttoaineID)
                    VALUES (@Hinta, @Rekisteri_paivamaara, @Moottorin_tilavuus, @Mittarilukema, @AutonMerkkiID, @AutonMalliID, @VaritID, @PolttoaineID);";

            SqlCommand command = new(query, dbYhteys);
            command.Parameters.AddWithValue("@Hinta", auto.Hinta);
            command.Parameters.AddWithValue("@Rekisteri_paivamaara", auto.Rekisteri_paivamaara);
            command.Parameters.AddWithValue("@Moottorin_tilavuus", auto.Moottorin_tilavuus);
            command.Parameters.AddWithValue("@Mittarilukema", auto.Mittarilukema);
            command.Parameters.AddWithValue("@AutonMerkkiID", auto.AutonMerkkiID);
            command.Parameters.AddWithValue("@AutonMalliID", auto.AutonMalliID);
            command.Parameters.AddWithValue("@VaritID", auto.VaritID);
            command.Parameters.AddWithValue("@PolttoaineID", auto.PolttoaineID);

            command.ExecuteNonQuery();

            Debug.WriteLine("auto added to database with:" +
                "Hinta: " + auto.Hinta +
                "Rekisteri_paivamaara: " + auto.Rekisteri_paivamaara +
                "Moottorin_tilavuus: " + auto.Moottorin_tilavuus +
                "Mittarilukema: " + auto.Mittarilukema +
                "AutonMerkkiID: " + auto.AutonMerkkiID +
                "AutonMalliID: " + auto.AutonMalliID +
                "VaritID: " + auto.VaritID +
                "PolttoaineID: " + auto.PolttoaineID);
            DisconnectDatabase();
        }

        //internal List<Auto> GetAutotFromMerkki(string merkki)
        //{
        //    if (ConnectDatabase())
        //    {
        //        string query = @"SELECT * FROM auto
        //                        WHERE AutonMerkkiID = "
        //                        + GetAutonMerkkiIDFromText(merkki)
        //                        + ";";
        //        SqlCommand command = new(query, dbYhteys);
        //        reader = command.ExecuteReader();
        //        List<Auto> autot = new();
        //        while (reader.Read())
        //        {
        //            Auto auto = new()
        //            {
        //                ID = reader.GetInt32(0),
        //                Hinta = reader.GetDecimal(1),
        //                Rekisteri_paivamaara = reader.GetDateTime(2),
        //                Moottorin_tilavuus = reader.GetDecimal(3),
        //                Mittarilukema = reader.GetInt32(4),
        //                AutonMerkkiID = reader.GetInt32(5),
        //                AutonMalliID = reader.GetInt32(6),
        //                VaritID = reader.GetInt32(7),
        //                PolttoaineID = reader.GetInt32(8)
        //            };
        //            autot.Add(auto);
        //        }
        //        DisconnectDatabase();
        //        return autot;
        //    }
        //    else
        //    {
        //        throw new Exception("Database connection failed");
        //    }
        //}
    }
}
