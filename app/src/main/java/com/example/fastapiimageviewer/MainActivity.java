package com.example.fastapiimageviewer;

import android.os.Bundle;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;


import com.example.fastapiimageviewer.network.ApiService;
import com.example.fastapiimageviewer.models.Image;
import com.example.fastapiimageviewer.adapters.ImageAdapter;
import com.example.fastapiimageviewer.network.RetrofitClient;

import java.util.List;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class MainActivity extends AppCompatActivity {
    private RecyclerView recyclerView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        recyclerView = findViewById(R.id.recyclerView);
        recyclerView.setLayoutManager(new LinearLayoutManager(this));

        // Создание API-сервиса
        ApiService apiService = RetrofitClient.getRetrofitInstance().create(ApiService.class);

        // Получение списка изображений
        apiService.getImages().enqueue(new Callback<List<Image>>() {
            @Override
            public void onResponse(Call<List<Image>> call, Response<List<Image>> response) {
                if (response.isSuccessful() && response.body() != null) {
                    new ImageAdapter(MainActivity.this, response.body());


                } else {
                    Toast.makeText(MainActivity.this, "No images found", Toast.LENGTH_SHORT).show();
                }
            }

            @Override
            public void onFailure(Call<List<Image>> call, Throwable t) {
                Toast.makeText(MainActivity.this, "Failed to load images", Toast.LENGTH_SHORT).show();
            }
        });
    }
}
