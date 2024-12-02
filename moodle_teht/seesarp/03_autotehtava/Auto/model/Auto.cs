using System;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace Autokauppa.model
{
    public class Auto
    {
        [Key]
        public int ID { get; set; }
        public Decimal Hinta { get; set; }
        public DateTime Rekisteri_paivamaara { get; set; }
        public Decimal Moottorin_tilavuus { get; set; }
        public int Mittarilukema { get; set; }
        public int AutonMerkkiID { get; set; }
        public int AutonMalliID { get; set; }
        public int VaritID { get; set; }
        public int PolttoaineID { get; set; }
    }

    public class AutonMallit
    {
        [Key]
        public int ID { get; set; }

        [Column("Auton_mallin_nimi")]
        public string AutonMalli { get; set; }
        public int AutonMerkkiID { get; set; }
    }

    public class AutonMerkki
    {
        [Key]
        public int ID { get; set; }
        public string Merkki { get; set; }
    }

    public class Polttoaine
    {
        [Key]
        public int ID { get; set; }

        [Column("Polttoaineen_nimi")]
        public string PolttoaineNimi { get; set; }
    }

    public class Varit
    {
        [Key]
        public int ID { get; set; }

        [Column("Varin_nimi")]
        public string Vari { get; set; }
    }
}
