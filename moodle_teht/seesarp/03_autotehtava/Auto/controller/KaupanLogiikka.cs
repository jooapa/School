using Autokauppa.model;
using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Autokauppa.controller
{
    public class KaupanLogiikka
    {
        DatabaseHallinta dbModel = new();

        public bool TestDatabaseConnection()
        {
            return dbModel.ConnectDatabase();
        }

        public bool SaveAuto(model.Auto newAuto) 
        {
            bool didItGoIntoDatabase = dbModel.SaveAutoIntoDatabase(newAuto);
            return didItGoIntoDatabase;
        }


        public Auto GetAutoFromDatabase(int id)
        {
            //int length = dbModel.GetLength() - 1;

            //if (id < 1)
            //{
            //    //MessageBox.Show("id < 1" + id);
            //    return dbModel.GetAutoFromDatabase(dbModel.GetAutoHintaLastID());
            //}
            //else if (id > length)
            //{
            //    //MessageBox.Show("id > len" + id);
            //    return dbModel.GetAutoFromDatabase(dbModel.GetAutoHintaFirstID());
            //}
            //else
            //{
                //MessageBox.Show("id gay" + id);
                return dbModel.GetAutoFromDatabase(id);
            //}
        }

        internal string GetAutonMalliNimi(int autonMalliID)
        {
            return dbModel.GetAutonMalli(autonMalliID);
        }

        internal string GetAutonMerkkiNimi(int autonMerkkiID)
        {
            return dbModel.GetAutonMerkki(autonMerkkiID);
        }

        internal string GetPolttoaineNimi(int polttoaineID)
        {
            return dbModel.GetPolttoaine(polttoaineID);
        }

        internal string GetVariNimi(int varitID)
        {
            return dbModel.GetVari(varitID);
        }
        internal List<AutonMallit> GetAutonMallit()
        {
            return dbModel.GetAutonMallit();
        }

        internal List<AutonMerkki> GetAutonMerkit()
        {
            return dbModel.GetAutonMerkit();
        }

        internal List<Polttoaine> GetPolttoaineet()
        {
            return dbModel.GetPolttoaineet();
        }

        internal List<Varit> GetVarit()
        {
            return dbModel.GetVarit();
        }

        internal int GetAutonMalliIDFromText(string text)
        {
            return dbModel.GetAutonMalliIDFromText(text);
        }

        internal int GetAutonMerkkiIDFromText(string text)
        {
            return dbModel.GetAutonMerkkiIDFromText(text);
        }

        internal int GetPolttoaineIDFromText(string text)
        {
            return dbModel.GetPolttoaineIDFromText(text);
        }

        internal int GetVariIDFromText(string text)
        {
            return dbModel.GetVariIDFromText(text);
        }

        internal void UpdateAuto(Auto auto)
        {
            dbModel.UpdateAuto(auto);
        }

        internal int GetAutoCountID()
        {
            return dbModel.GetAutoCountID();
        }

        internal void DeleteAuto(int id)
        {
            dbModel.DeleteAuto(id);
        }

        internal void AddNewAuto(Auto auto)
        {
            dbModel.AddNewAuto(auto);
        }
    }
}
