package com.example.fastapiimageviewer.network;



import com.example.fastapiimageviewer.models.Image;

import java.util.List;

import retrofit2.Call;
import retrofit2.http.GET;

public interface ApiService {
    @GET("/images/")
    Call<List<Image>> getImages();
}
