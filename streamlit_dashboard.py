import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.set_option('deprecation.showfileUploaderEncoding', False)


st.title("Aplikasi Visualisasi Data")

st.sidebar.subheader("Pengaturan Visualisasi")

uploaded_file = st.sidebar.file_uploader(label="Upload file CSV anda", type=['csv'])
show_data = st.sidebar.checkbox("Tampilkan Data")

chart_select = st.sidebar.selectbox(
	label="Pilih Jenis Chart",
	options=['Barplot', 'Histogram', 'Piechart', 'Scatterplot'])


if uploaded_file is not None:
	df = pd.read_csv(uploaded_file)

try:
	if show_data:
		st.write(df)
	if chart_select == 'Barplot':
		color_plot = st.sidebar.selectbox(
			label="Pilih Warna Chart",
			options=['blue', 'red', 'green', 'black'])
		column_select = st.sidebar.selectbox(
			label="Pilih Kolom",
			options=['childNum', 'gender']
			)
		if column_select == 'gender':
			# Hitung jumlah gender dari kolom gender
			jumlah_anak_per_gender = df['gender'].value_counts()

			# Gambar diagram batang
			jumlah_anak_per_gender.plot(kind='bar', title='Jumlah Anak per Gender', color=color_plot)
			plt.xlabel('Gender')
			plt.ylabel('Jumlah Anak')
			st.pyplot(plt)

		elif column_select == 'childNum':
			# Ambil kolom yang dibutuhkan
			families = df[['family', 'children']].drop_duplicates()
			# Hitung jumlah keluarga yang memiliki jumlah anak tertentu, diurutkan berdasarkan jumlah anak
			jumlah_anak = families['children'].value_counts().sort_index()

			# Gambar diagram batang
			jumlah_anak.plot(kind='bar', title='Jumlah Anak dalam Keluarga', color=color_plot)
			plt.xlabel('Jumlah Anak')
			plt.ylabel('Jumlah Keluarga')
			st.pyplot(plt)

	elif chart_select == 'Histogram':
		color_plot = st.sidebar.selectbox(
			label="Pilih Warna Chart",
			options=['blue', 'red', 'green', 'black'])
		column_select = st.sidebar.selectbox(
			label="Pilih Kolom",
			options=['father', 'mother', 'midparentHeight', 'childHeight']
			)
		title_dict = {'father': 'Tinggi Ayah',
					  'mother': 'Tinggi Ibu',
					  'midparentHeight':'Kombinasi Tinggi Ayah & Ibu',
					  'childHeight':'Tinggi Anak'}
		bins_slider = st.sidebar.slider('Pilih jumlah bins', 10,50,1)
		df[column_select].plot.hist(title=title_dict[column_select], color=color_plot, bins=bins_slider)
		plt.xlabel('Tinggi')
		plt.ylabel('Frekuensi')
		st.pyplot(plt)

	elif chart_select == "Piechart":
		color_1 = st.sidebar.selectbox(
			label="Pilih Warna Pertama",
			options=['blue', 'red', 'green', 'black'])
		color_2 = st.sidebar.selectbox(
			label="Pilih Warna Kedua",
			options=['blue', 'red', 'green', 'black'])
		jumlah_anak_per_gender = df['gender'].value_counts()

		jumlah_anak_per_gender.plot(kind='pie', title='Jumlah Anak per Gender', colors=[color_1,color_2])
		plt.legend()
		st.pyplot(plt)
	elif chart_select == "Scatterplot":
		column_x = st.sidebar.selectbox(
			label="Pilih Kolom Sumbu X",
			options=['father', 'mother', 'midparentHeight', 'childHeight']
			)
		column_y = st.sidebar.selectbox(
			label="Pilih Kolom Sumbu Y",
			options=['father', 'mother', 'midparentHeight', 'childHeight']
			)
		color_plot = st.sidebar.selectbox(
			label="Pilih Warna Chart",
			options=['blue', 'red', 'green', 'black'])

		selected_df = df[[column_x, column_y]]

		# buat scatterplot
		selected_df.plot(kind='scatter', title=f'{column_x} vs {column_y}', x=column_x, y=column_y, color=color_plot)
		plt.xlabel('midparentHeight')
		plt.ylabel('childHeight')
		st.pyplot(plt)

except Exception as e:
	st.write("Silahkan Upload File Anda")





