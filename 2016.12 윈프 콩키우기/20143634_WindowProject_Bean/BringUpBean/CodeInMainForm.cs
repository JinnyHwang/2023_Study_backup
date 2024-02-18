using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace BringUpBean
{
    public partial class CodeInMainForm : Form
    {
        string sendmessage = "";

        public CodeInMainForm()
        {
            InitializeComponent();
        }

        private void btnOk_Click(object sender, EventArgs e)
        {
            //메세지를 변수에 저장하여 이 폼의 종료지점으로 가서 MainForm에 적용
            sendmessage = txtSendBean.Text;
            Close();
        }

        public string Sendmessage
        {
            get { return sendmessage; }
        }
    }
}
