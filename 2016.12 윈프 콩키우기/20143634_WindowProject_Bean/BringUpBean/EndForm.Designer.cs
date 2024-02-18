namespace BringUpBean
{
    partial class EndForm
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
            this.components = new System.ComponentModel.Container();
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(EndForm));
            this.picBoxEnd = new System.Windows.Forms.PictureBox();
            this.label1 = new System.Windows.Forms.Label();
            this.lblFinalBean = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.btnNewBean = new System.Windows.Forms.Button();
            this.imgListBeanEnding = new System.Windows.Forms.ImageList(this.components);
            ((System.ComponentModel.ISupportInitialize)(this.picBoxEnd)).BeginInit();
            this.SuspendLayout();
            // 
            // picBoxEnd
            // 
            this.picBoxEnd.Location = new System.Drawing.Point(176, 105);
            this.picBoxEnd.Name = "picBoxEnd";
            this.picBoxEnd.Size = new System.Drawing.Size(195, 183);
            this.picBoxEnd.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.picBoxEnd.TabIndex = 0;
            this.picBoxEnd.TabStop = false;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("NanumBarunpen", 19.8F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(129)));
            this.label1.Location = new System.Drawing.Point(12, 41);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(159, 42);
            this.label1.TabIndex = 1;
            this.label1.Text = "당신의 콩은";
            // 
            // lblFinalBean
            // 
            this.lblFinalBean.AutoSize = true;
            this.lblFinalBean.Font = new System.Drawing.Font("NanumBarunpen", 19.8F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(129)));
            this.lblFinalBean.ForeColor = System.Drawing.Color.LightSeaGreen;
            this.lblFinalBean.Location = new System.Drawing.Point(181, 41);
            this.lblFinalBean.Name = "lblFinalBean";
            this.lblFinalBean.Size = new System.Drawing.Size(70, 42);
            this.lblFinalBean.TabIndex = 2;
            this.lblFinalBean.Text = "뭐뭐";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Font = new System.Drawing.Font("NanumBarunpen", 19.8F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(129)));
            this.label3.Location = new System.Drawing.Point(356, 41);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(248, 42);
            this.label3.TabIndex = 3;
            this.label3.Text = "(이)가 되었습니다!";
            // 
            // btnNewBean
            // 
            this.btnNewBean.Font = new System.Drawing.Font("Nanum Pen Script", 19.8F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(129)));
            this.btnNewBean.ForeColor = System.Drawing.Color.DarkCyan;
            this.btnNewBean.Location = new System.Drawing.Point(176, 331);
            this.btnNewBean.Name = "btnNewBean";
            this.btnNewBean.Size = new System.Drawing.Size(195, 43);
            this.btnNewBean.TabIndex = 4;
            this.btnNewBean.Text = "새로키우기";
            this.btnNewBean.UseVisualStyleBackColor = true;
            this.btnNewBean.Click += new System.EventHandler(this.btnNewBean_Click);
            // 
            // imgListBeanEnding
            // 
            this.imgListBeanEnding.ImageStream = ((System.Windows.Forms.ImageListStreamer)(resources.GetObject("imgListBeanEnding.ImageStream")));
            this.imgListBeanEnding.TransparentColor = System.Drawing.Color.Transparent;
            this.imgListBeanEnding.Images.SetKeyName(0, "plain");
            this.imgListBeanEnding.Images.SetKeyName(1, "Big");
            this.imgListBeanEnding.Images.SetKeyName(2, "Painter");
            this.imgListBeanEnding.Images.SetKeyName(3, "progamer");
            this.imgListBeanEnding.Images.SetKeyName(4, "programmer");
            // 
            // EndForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.Color.Ivory;
            this.ClientSize = new System.Drawing.Size(621, 411);
            this.Controls.Add(this.btnNewBean);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.lblFinalBean);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.picBoxEnd);
            this.ForeColor = System.Drawing.Color.DimGray;
            this.Name = "EndForm";
            this.Text = "콩이 다 자랐습니다";
            this.Load += new System.EventHandler(this.EndForm_Load);
            ((System.ComponentModel.ISupportInitialize)(this.picBoxEnd)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.PictureBox picBoxEnd;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label lblFinalBean;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Button btnNewBean;
        private System.Windows.Forms.ImageList imgListBeanEnding;
    }
}