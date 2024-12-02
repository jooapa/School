using System;
using System.Data;
using Microsoft.Data.SqlClient;
using System.Windows.Forms;


namespace T1
{
    public partial class Form1 : Form
    {
        string connectionString =
            "Server=(localdb)\\MSSQLLocalDB;" +
            "Database=T1;" +
            "Trusted_Connection=True;";

        public Form1()
        {
            InitializeComponent();

            // add data to combobox
            string query = "SELECT ryhmannimi FROM opiskelijaryhma";
            using (SqlConnection connection = new SqlConnection(connectionString))
            {
                SqlCommand command = new SqlCommand(query, connection);
                connection.Open();
                SqlDataReader reader = command.ExecuteReader();
                while (reader.Read())
                {
                    comboBox1.Items.Add(reader.GetString(0));
                }
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            // get data from database
            string query = "SELECT * FROM opiskelija";
            using SqlConnection connection = new SqlConnection(connectionString);
            SqlDataAdapter adapter = new SqlDataAdapter(query, connection);
            DataTable table = new DataTable();
            adapter.Fill(table);
            dataGridView1.DataSource = table;
        }

        /// <summary>
        /// Lis‰‰ oppilas
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void button2_Click(object sender, EventArgs e)
        {
            using SqlConnection connection = new(connectionString);

            // get the data from the textboxes
            string etunimi = textBox2.Text;
            string sukunimi = textBox1.Text;
            string ryhmannimi = comboBox1.Text;

            if (etunimi == "" || sukunimi == "" || ryhmannimi == "")
                return;

            // if ryhm‰ exists
            string query = "SELECT id FROM opiskelijaryhma WHERE ryhmannimi = @ryhmannimi";
            SqlCommand command = new(query, connection);
            command.Parameters.AddWithValue("@ryhmannimi", ryhmannimi);
            connection.Open();
            // if value is null, return
            if (command.ExecuteScalar() == null)
            {
                connection.Close();
                return;
            }
            int ryhmanro = (int)command.ExecuteScalar();
            command.ExecuteScalar();
            connection.Close();

            if (ryhmanro == 0)
                return;

            // insert data to database
            query = "INSERT INTO opiskelija (etunimi, sukunimi, ryhma_id) VALUES (@etunimi, @sukunimi, @ryhmanro)";
            command = new(query, connection);

            command.Parameters.AddWithValue("@etunimi", etunimi);
            command.Parameters.AddWithValue("@sukunimi", sukunimi);
            command.Parameters.AddWithValue("@ryhmanro", ryhmanro);

            connection.Open();
            command.ExecuteNonQuery();
            connection.Close();

            // clear textboxes
            textBox1.Clear();
            textBox2.Clear();

        }

        private void button3_Click(object sender, EventArgs e)
        {
            // get the numericUpDown1
            int id = (int)numericUpDown1.Value;

            // delete the student
            string query = "DELETE FROM opiskelija WHERE id = @id";
            using SqlConnection connection = new(connectionString);
            SqlCommand command = new(query, connection);
            command.Parameters.AddWithValue("@id", id);
            connection.Open();
            command.ExecuteNonQuery();
            connection.Close();

            // clear the numericUpDown1 
            numericUpDown1.Value = 0;
        }
    }
}
