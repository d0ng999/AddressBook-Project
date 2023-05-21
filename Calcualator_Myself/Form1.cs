using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Web;
using System.Windows.Forms;
using System.Text.RegularExpressions;
using System.Xml.Schema;

namespace Calcualator_Myself
{
    
    public enum Operators { Add, Sub, Multi, Div, Equal, Double, Sqrt, OneDiv};

    public partial class Form1 : Form
    {
        public bool isNewNum = true;
        public Operators Opt = Operators.Add;
        public double Result = 0;
        public double Res = 0;
        public double SecondValue = 0;
        public bool ishave = true;
        public int count_dot = 0;
        public int count_Equal = 0;


        public Form1()
        {
            InitializeComponent();
        }

        private void button22_Click(object sender, EventArgs e)
        {
            Button numButton = (Button)sender;
            SetNum(numButton.Text);
        }

        public void SetNum(string num)
        {
            if (isNewNum)
            {
                NumScreen1.Text = num;
                if (ishave = NumScreen1.Text.Contains("."))
                    count_dot = 1;
                else
                    count_dot = 0;
                if (ishave = NumScreen2.Text.Contains("="))
                {
                    NumScreen2.Text = "";
                }
                if (Result == 0)
                {
                    NumScreen2.Text = "";
                }

                isNewNum = false;
            }

            else
            {
                NumScreen1.Text += num;
            }
        }

        private void button20_Click(object sender, EventArgs e)
        {
            double num = double.Parse(NumScreen1.Text);
            this.SecondValue = double.MinValue;
            //const double num2 = num;

            if (isNewNum == false)
            {

                if (Opt == Operators.Add)
                {
                    Result += num;
                }
                else if (Opt == Operators.Sub)
                {
                    Result -= num;
                }
                else if (Opt == Operators.Multi)
                {
                    Result *= num;
                }
                else if (Opt == Operators.Div)
                {
                    Result /= num;
                }
                else if (Opt == Operators.Equal)
                {
                    NumScreen1.Text = Result.ToString();
                    Result = num;

                }

                isNewNum = true;
            }

            NumScreen1.Text = Result.ToString();

            Button mark = (Button)sender;

            if (mark.Text == "+")
            {
                Opt = Operators.Add;
                NumScreen2.Text += num;
                NumScreen2.Text += mark.Text;
                if (ishave = NumScreen2.Text.Contains("="))
                {
                    NumScreen2.Text = num.ToString() + "+";
                    NumScreen1.Text = "";
                }

            }
            else if (mark.Text == "-")
            {
                Opt = Operators.Sub;
                NumScreen2.Text += num;
                NumScreen2.Text += mark.Text;
                if (ishave = NumScreen2.Text.Contains("="))
                {
                    NumScreen2.Text = num.ToString() + "-";
                }

            }
            else if(mark.Text == "*")
            {
                Opt = Operators.Multi;
                NumScreen2.Text += num;
                NumScreen2.Text += mark.Text;
                if (ishave = NumScreen2.Text.Contains("="))
                {
                    NumScreen2.Text = num.ToString() + "*";
                }

            }
            else if(mark.Text == "/")
            {
                Opt = Operators.Div;
                NumScreen2.Text += num;
                NumScreen2.Text += mark.Text;
                if (ishave = NumScreen2.Text.Contains("="))
                {
                    NumScreen2.Text = num.ToString() + "/";
                }

            }
            else if (mark.Text == "=")
            {
                Opt = Operators.Equal;
                MatchCollection matches = Regex.Matches(NumScreen2.Text, "=");
                int cnt = matches.Count;
                //count_Equal += 1;
                
                //if (count_Equal>1)
                //{
                //    if (ishave = NumScreen2.Text.Contains("+"))
                //    {
                //        NumScreen2.Text = Res.ToString() + "+" + num2;
                //        NumScreen1.Text = (Res + num2).ToString();
                //    }
                //}

                if (cnt == 1)
                {
                    NumScreen2.Text = NumScreen2.Text;
                }
                else
                {
                    NumScreen2.Text += num;
                    NumScreen2.Text += mark.Text;
                    Res = double.Parse(NumScreen1.Text);
                }
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            NumScreen1.Text = "0";
            NumScreen2.Text = "";
            Result = 0;
            isNewNum = true;
        }

        private void button5_Click(object sender, EventArgs e)
        {
            
            double num = double.Parse(NumScreen1.Text);
            if (num == 0)
            {
                NumScreen1.Text = "0은 나눌 수 없습니다";
            }
            else
            {
                Result = 1 / num;
                NumScreen1.Text = Result.ToString();
                NumScreen2.Text = ("1/" + num);
                isNewNum = true;
                Result = 0;
            }

        }

        private void button6_Click(object sender, EventArgs e)
        {
            double num = double.Parse(NumScreen1.Text);
            Result = num * num;
            NumScreen1.Text = Result.ToString();
            NumScreen2.Text = ("sqr(" + num + ")");
            isNewNum = true;
            Result = 0;
        }

        private void button7_Click(object sender, EventArgs e)
        {
            double num = double.Parse(NumScreen1.Text);
            Result = Math.Sqrt(num);
            NumScreen1.Text = Result.ToString();
            NumScreen2.Text = ("sqrt(" + num + ")");
            isNewNum = true;
            Result = 0;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            NumScreen1.Text = "0";
            isNewNum = true;
        }

        private void button4_Click(object sender, EventArgs e)
        {
            int len = NumScreen1.Text.Length;
            NumScreen1.Text = NumScreen1.Text.Remove(len-1, 1);
        }

        private void button23_Click(object sender, EventArgs e)
        {
            count_dot += 1;   
            if (count_dot == 1)
            {
                NumScreen1.Text += ".";
            }
        }

        private void button21_Click(object sender, EventArgs e)
        {
            double num = double.Parse(NumScreen1.Text);
            num = num*(-1);
            NumScreen1.Text = num.ToString();
            
            if (ishave == NumScreen2.Text.Contains("="))
            {
                NumScreen2.Text = "";                
            }
            Result = num;
            isNewNum = true;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            double num = double.Parse(NumScreen1.Text);
            Result = num * (0.01);
            NumScreen1.Text = Result.ToString();

        }

        //private void button22_KeyDown(object sender, KeyEventArgs e)
        //{
        //    double num = double.Parse(NumScreen1.Text);
        //    if (isNewNum == false)
        //    {

        //        if (Opt == Operators.Add)
        //        {
        //            Result += num;
        //        }
        //        else if (Opt == Operators.Sub)
        //        {
        //            Result -= num;
        //        }
        //        else if (Opt == Operators.Multi)
        //        {
        //            Result *= num;
        //        }
        //        else if (Opt == Operators.Div)
        //        {
        //            Result /= num;
        //        }
        //        else if (Opt == Operators.Equal)
        //        {
        //            NumScreen1.Text = Result.ToString();
        //            Result = num;
        //        }

        //        isNewNum = true;
        //    }

        //    string num1 = e.KeyData.ToString().Replace("NumPad", "");
        //    if ((e.KeyCode == Keys.NumPad0 || e.KeyCode == Keys.NumPad1 || e.KeyCode == Keys.NumPad2 || e.KeyCode == Keys.NumPad3 ||
        //       e.KeyCode == Keys.NumPad4 || e.KeyCode == Keys.NumPad5 || e.KeyCode == Keys.NumPad6 || e.KeyCode == Keys.NumPad7 ||
        //       e.KeyCode == Keys.NumPad8 || e.KeyCode == Keys.NumPad9) && isNewNum)
        //    {
        //        NumScreen1.Text += num1;
        //    }
        //    else if(e.KeyCode == Keys.Add)
        //    {
        //        Opt = Operators.Multi;
        //        NumScreen2.Text += NumScreen1.Text;
        //        NumScreen2.Text += "+";
        //        if (ishave = NumScreen2.Text.Contains("="))
        //        {
        //            NumScreen2.Text = this.Result + "+";
        //        }
        //        NumScreen1.Text = "";
        //    }
        //    isNewNum = true;

        //}

        //private void button14_KeyPress(object sender, KeyPressEventArgs e)
        //{
        //    if (e.KeyChar == (int)Keys.NumPad0)
        //    {
        //        NumScreen1.Text += e.KeyChar;
        //    }
        //}
    }   
}
