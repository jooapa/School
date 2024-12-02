namespace Autokauppa.view
{
    partial class MainMenu
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            btnSeuraava = new System.Windows.Forms.Button();
            gbAuto = new System.Windows.Forms.GroupBox();
            mittariLabel = new System.Windows.Forms.Label();
            tilavuusLabel = new System.Windows.Forms.Label();
            rekisteriLabel = new System.Windows.Forms.Label();
            pricaLabel = new System.Windows.Forms.Label();
            polttoaineLabel = new System.Windows.Forms.Label();
            cbPolttoaine = new System.Windows.Forms.ComboBox();
            label3 = new System.Windows.Forms.Label();
            cbVari = new System.Windows.Forms.ComboBox();
            label2 = new System.Windows.Forms.Label();
            cbMalli = new System.Windows.Forms.ComboBox();
            dtpPaiva = new System.Windows.Forms.DateTimePicker();
            tbHinta = new System.Windows.Forms.TextBox();
            tbMittari = new System.Windows.Forms.TextBox();
            tbMottoriTlv = new System.Windows.Forms.TextBox();
            tbId = new System.Windows.Forms.TextBox();
            label1 = new System.Windows.Forms.Label();
            cbMerkki = new System.Windows.Forms.ComboBox();
            btnEdellinen = new System.Windows.Forms.Button();
            menuStrip1 = new System.Windows.Forms.MenuStrip();
            exitToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            exitToolStripMenuItem1 = new System.Windows.Forms.ToolStripMenuItem();
            aboutToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            testaaTietokantaaToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            btnLisaa = new System.Windows.Forms.Button();
            btnTallenna = new System.Windows.Forms.Button();
            btnPoista = new System.Windows.Forms.Button();
            gbAuto.SuspendLayout();
            menuStrip1.SuspendLayout();
            SuspendLayout();
            // 
            // btnSeuraava
            // 
            btnSeuraava.Location = new System.Drawing.Point(111, 388);
            btnSeuraava.Margin = new System.Windows.Forms.Padding(3, 4, 3, 4);
            btnSeuraava.Name = "btnSeuraava";
            btnSeuraava.Size = new System.Drawing.Size(89, 41);
            btnSeuraava.TabIndex = 17;
            btnSeuraava.Text = "Seuraava";
            btnSeuraava.UseVisualStyleBackColor = true;
            btnSeuraava.Click += btnSeuraava_Click;
            // 
            // gbAuto
            // 
            gbAuto.Controls.Add(mittariLabel);
            gbAuto.Controls.Add(tilavuusLabel);
            gbAuto.Controls.Add(rekisteriLabel);
            gbAuto.Controls.Add(pricaLabel);
            gbAuto.Controls.Add(polttoaineLabel);
            gbAuto.Controls.Add(cbPolttoaine);
            gbAuto.Controls.Add(label3);
            gbAuto.Controls.Add(cbVari);
            gbAuto.Controls.Add(label2);
            gbAuto.Controls.Add(cbMalli);
            gbAuto.Controls.Add(dtpPaiva);
            gbAuto.Controls.Add(tbHinta);
            gbAuto.Controls.Add(tbMittari);
            gbAuto.Controls.Add(tbMottoriTlv);
            gbAuto.Controls.Add(tbId);
            gbAuto.Controls.Add(label1);
            gbAuto.Controls.Add(cbMerkki);
            gbAuto.Location = new System.Drawing.Point(12, 45);
            gbAuto.Margin = new System.Windows.Forms.Padding(3, 4, 3, 4);
            gbAuto.Name = "gbAuto";
            gbAuto.Padding = new System.Windows.Forms.Padding(3, 4, 3, 4);
            gbAuto.Size = new System.Drawing.Size(457, 250);
            gbAuto.TabIndex = 18;
            gbAuto.TabStop = false;
            gbAuto.Text = "Auton tiedot";
            gbAuto.Enter += gbAuto_Enter;
            // 
            // mittariLabel
            // 
            mittariLabel.AutoSize = true;
            mittariLabel.Location = new System.Drawing.Point(155, 98);
            mittariLabel.Name = "mittariLabel";
            mittariLabel.Size = new System.Drawing.Size(105, 20);
            mittariLabel.TabIndex = 33;
            mittariLabel.Text = "Mittari lukema";
            // 
            // tilavuusLabel
            // 
            tilavuusLabel.AutoSize = true;
            tilavuusLabel.Location = new System.Drawing.Point(159, 31);
            tilavuusLabel.Name = "tilavuusLabel";
            tilavuusLabel.Size = new System.Drawing.Size(100, 20);
            tilavuusLabel.TabIndex = 32;
            tilavuusLabel.Text = "Moottorin tilv";
            // 
            // rekisteriLabel
            // 
            rekisteriLabel.AutoSize = true;
            rekisteriLabel.Location = new System.Drawing.Point(17, 165);
            rekisteriLabel.Name = "rekisteriLabel";
            rekisteriLabel.Size = new System.Drawing.Size(98, 20);
            rekisteriLabel.TabIndex = 31;
            rekisteriLabel.Text = "Rekisteri pvm";
            // 
            // pricaLabel
            // 
            pricaLabel.AutoSize = true;
            pricaLabel.Location = new System.Drawing.Point(17, 98);
            pricaLabel.Name = "pricaLabel";
            pricaLabel.Size = new System.Drawing.Size(45, 20);
            pricaLabel.TabIndex = 30;
            pricaLabel.Text = "Hinta";
            // 
            // polttoaineLabel
            // 
            polttoaineLabel.AutoSize = true;
            polttoaineLabel.Location = new System.Drawing.Point(150, 165);
            polttoaineLabel.Name = "polttoaineLabel";
            polttoaineLabel.Size = new System.Drawing.Size(76, 20);
            polttoaineLabel.TabIndex = 29;
            polttoaineLabel.Text = "Polttoaine";
            // 
            // cbPolttoaine
            // 
            cbPolttoaine.FormattingEnabled = true;
            cbPolttoaine.Location = new System.Drawing.Point(150, 194);
            cbPolttoaine.Margin = new System.Windows.Forms.Padding(3, 4, 3, 4);
            cbPolttoaine.Name = "cbPolttoaine";
            cbPolttoaine.Size = new System.Drawing.Size(121, 28);
            cbPolttoaine.TabIndex = 28;
            // 
            // label3
            // 
            label3.AutoSize = true;
            label3.Location = new System.Drawing.Point(290, 165);
            label3.Name = "label3";
            label3.Size = new System.Drawing.Size(34, 20);
            label3.TabIndex = 27;
            label3.Text = "Väri";
            // 
            // cbVari
            // 
            cbVari.FormattingEnabled = true;
            cbVari.Location = new System.Drawing.Point(293, 194);
            cbVari.Margin = new System.Windows.Forms.Padding(3, 4, 3, 4);
            cbVari.Name = "cbVari";
            cbVari.Size = new System.Drawing.Size(121, 28);
            cbVari.TabIndex = 26;
            // 
            // label2
            // 
            label2.AutoSize = true;
            label2.Location = new System.Drawing.Point(289, 98);
            label2.Name = "label2";
            label2.Size = new System.Drawing.Size(42, 20);
            label2.TabIndex = 25;
            label2.Text = "Malli";
            // 
            // cbMalli
            // 
            cbMalli.FormattingEnabled = true;
            cbMalli.Location = new System.Drawing.Point(290, 125);
            cbMalli.Margin = new System.Windows.Forms.Padding(3, 4, 3, 4);
            cbMalli.Name = "cbMalli";
            cbMalli.Size = new System.Drawing.Size(121, 28);
            cbMalli.TabIndex = 24;
            // 
            // dtpPaiva
            // 
            dtpPaiva.Format = System.Windows.Forms.DateTimePickerFormat.Short;
            dtpPaiva.Location = new System.Drawing.Point(17, 195);
            dtpPaiva.Margin = new System.Windows.Forms.Padding(3, 4, 3, 4);
            dtpPaiva.Name = "dtpPaiva";
            dtpPaiva.Size = new System.Drawing.Size(116, 27);
            dtpPaiva.TabIndex = 23;
            // 
            // tbHinta
            // 
            tbHinta.Location = new System.Drawing.Point(17, 122);
            tbHinta.Margin = new System.Windows.Forms.Padding(3, 4, 3, 4);
            tbHinta.Name = "tbHinta";
            tbHinta.Size = new System.Drawing.Size(116, 27);
            tbHinta.TabIndex = 22;
            // 
            // tbMittari
            // 
            tbMittari.Location = new System.Drawing.Point(155, 125);
            tbMittari.Margin = new System.Windows.Forms.Padding(3, 4, 3, 4);
            tbMittari.Name = "tbMittari";
            tbMittari.Size = new System.Drawing.Size(116, 27);
            tbMittari.TabIndex = 21;
            // 
            // tbMottoriTlv
            // 
            tbMottoriTlv.Location = new System.Drawing.Point(155, 55);
            tbMottoriTlv.Margin = new System.Windows.Forms.Padding(3, 4, 3, 4);
            tbMottoriTlv.Name = "tbMottoriTlv";
            tbMottoriTlv.Size = new System.Drawing.Size(116, 27);
            tbMottoriTlv.TabIndex = 20;
            // 
            // tbId
            // 
            tbId.Location = new System.Drawing.Point(17, 55);
            tbId.Margin = new System.Windows.Forms.Padding(3, 4, 3, 4);
            tbId.Name = "tbId";
            tbId.ReadOnly = true;
            tbId.Size = new System.Drawing.Size(116, 27);
            tbId.TabIndex = 19;
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Location = new System.Drawing.Point(290, 31);
            label1.Name = "label1";
            label1.Size = new System.Drawing.Size(85, 20);
            label1.TabIndex = 18;
            label1.Text = "Automerkki";
            // 
            // cbMerkki
            // 
            cbMerkki.FormattingEnabled = true;
            cbMerkki.Location = new System.Drawing.Point(289, 54);
            cbMerkki.Margin = new System.Windows.Forms.Padding(3, 4, 3, 4);
            cbMerkki.Name = "cbMerkki";
            cbMerkki.Size = new System.Drawing.Size(121, 28);
            cbMerkki.TabIndex = 17;
            // 
            // btnEdellinen
            // 
            btnEdellinen.Location = new System.Drawing.Point(12, 388);
            btnEdellinen.Margin = new System.Windows.Forms.Padding(3, 4, 3, 4);
            btnEdellinen.Name = "btnEdellinen";
            btnEdellinen.Size = new System.Drawing.Size(93, 41);
            btnEdellinen.TabIndex = 19;
            btnEdellinen.Text = "Edellinen";
            btnEdellinen.UseVisualStyleBackColor = true;
            btnEdellinen.Click += btnEdellinen_Click;
            // 
            // menuStrip1
            // 
            menuStrip1.ImageScalingSize = new System.Drawing.Size(20, 20);
            menuStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] { exitToolStripMenuItem, aboutToolStripMenuItem });
            menuStrip1.Location = new System.Drawing.Point(0, 0);
            menuStrip1.Name = "menuStrip1";
            menuStrip1.Size = new System.Drawing.Size(509, 28);
            menuStrip1.TabIndex = 20;
            menuStrip1.Text = "menuStrip1";
            // 
            // exitToolStripMenuItem
            // 
            exitToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] { exitToolStripMenuItem1 });
            exitToolStripMenuItem.Name = "exitToolStripMenuItem";
            exitToolStripMenuItem.Size = new System.Drawing.Size(81, 24);
            exitToolStripMenuItem.Text = "Tiedosto";
            // 
            // exitToolStripMenuItem1
            // 
            exitToolStripMenuItem1.Name = "exitToolStripMenuItem1";
            exitToolStripMenuItem1.Size = new System.Drawing.Size(131, 26);
            exitToolStripMenuItem1.Text = "Poistu";
            exitToolStripMenuItem1.Click += exitToolStripMenuItem1_Click;
            // 
            // aboutToolStripMenuItem
            // 
            aboutToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] { testaaTietokantaaToolStripMenuItem });
            aboutToolStripMenuItem.Name = "aboutToolStripMenuItem";
            aboutToolStripMenuItem.Size = new System.Drawing.Size(74, 24);
            aboutToolStripMenuItem.Text = "Muuta...";
            // 
            // testaaTietokantaaToolStripMenuItem
            // 
            testaaTietokantaaToolStripMenuItem.Name = "testaaTietokantaaToolStripMenuItem";
            testaaTietokantaaToolStripMenuItem.Size = new System.Drawing.Size(213, 26);
            testaaTietokantaaToolStripMenuItem.Text = "Testaa tietokantaa";
            testaaTietokantaaToolStripMenuItem.Click += testaaTietokantaaToolStripMenuItem_Click;
            // 
            // btnLisaa
            // 
            btnLisaa.Location = new System.Drawing.Point(396, 388);
            btnLisaa.Margin = new System.Windows.Forms.Padding(3, 4, 3, 4);
            btnLisaa.Name = "btnLisaa";
            btnLisaa.Size = new System.Drawing.Size(89, 41);
            btnLisaa.TabIndex = 21;
            btnLisaa.Text = "Lisää";
            btnLisaa.UseVisualStyleBackColor = true;
            btnLisaa.Click += btnLisaa_Click;
            // 
            // btnTallenna
            // 
            btnTallenna.Location = new System.Drawing.Point(206, 388);
            btnTallenna.Margin = new System.Windows.Forms.Padding(3, 4, 3, 4);
            btnTallenna.Name = "btnTallenna";
            btnTallenna.Size = new System.Drawing.Size(89, 41);
            btnTallenna.TabIndex = 23;
            btnTallenna.Text = "Tallenna";
            btnTallenna.UseVisualStyleBackColor = true;
            btnTallenna.Click += btnTallenna_Click;
            // 
            // btnPoista
            // 
            btnPoista.Location = new System.Drawing.Point(301, 388);
            btnPoista.Margin = new System.Windows.Forms.Padding(3, 4, 3, 4);
            btnPoista.Name = "btnPoista";
            btnPoista.Size = new System.Drawing.Size(89, 41);
            btnPoista.TabIndex = 24;
            btnPoista.Text = "Poista";
            btnPoista.UseVisualStyleBackColor = true;
            btnPoista.Click += btnPoista_Click;
            // 
            // MainMenu
            // 
            AutoScaleDimensions = new System.Drawing.SizeF(8F, 20F);
            AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            ClientSize = new System.Drawing.Size(509, 470);
            Controls.Add(btnPoista);
            Controls.Add(btnTallenna);
            Controls.Add(btnLisaa);
            Controls.Add(btnEdellinen);
            Controls.Add(gbAuto);
            Controls.Add(btnSeuraava);
            Controls.Add(menuStrip1);
            MainMenuStrip = menuStrip1;
            Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            Name = "MainMenu";
            Text = "MainMenu";
            Load += MainMenu_Load;
            gbAuto.ResumeLayout(false);
            gbAuto.PerformLayout();
            menuStrip1.ResumeLayout(false);
            menuStrip1.PerformLayout();
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion
        private System.Windows.Forms.Button btnSeuraava;
        private System.Windows.Forms.GroupBox gbAuto;
        private System.Windows.Forms.Label polttoaineLabel;
        private System.Windows.Forms.ComboBox cbPolttoaine;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.ComboBox cbVari;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.ComboBox cbMalli;
        private System.Windows.Forms.DateTimePicker dtpPaiva;
        private System.Windows.Forms.TextBox tbHinta;
        private System.Windows.Forms.TextBox tbMittari;
        private System.Windows.Forms.TextBox tbMottoriTlv;
        private System.Windows.Forms.TextBox tbId;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.ComboBox cbMerkki;
        private System.Windows.Forms.Button btnEdellinen;
        private System.Windows.Forms.MenuStrip menuStrip1;
        private System.Windows.Forms.ToolStripMenuItem exitToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem exitToolStripMenuItem1;
        private System.Windows.Forms.ToolStripMenuItem aboutToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem testaaTietokantaaToolStripMenuItem;
        private System.Windows.Forms.Button btnLisaa;
        private System.Windows.Forms.Label mittariLabel;
        private System.Windows.Forms.Label tilavuusLabel;
        private System.Windows.Forms.Label rekisteriLabel;
        private System.Windows.Forms.Label pricaLabel;
        private System.Windows.Forms.Button btnTallenna;
        private System.Windows.Forms.Button btnPoista;
    }
}