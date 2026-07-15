package org.example;

import org.springframework.http.MediaType;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.time.format.DateTimeFormatter;
import java.util.List;

@RestController
public class DatosController {

    private final JdbcTemplate jdbcTemplate;

    public DatosController(JdbcTemplate jdbcTemplate) {
        this.jdbcTemplate = jdbcTemplate;
    }

    @GetMapping(value = "/datos", produces = MediaType.TEXT_PLAIN_VALUE)
    public String obtenerDatos() {
        List<String> filas = jdbcTemplate.query(
                "SELECT usuario, accion, fecha, hora, short FROM redes ORDER BY id",
                (rs, rowNum) -> String.format(
                        "%s, %s, %s, %s, %s",
                        rs.getString("usuario"),
                        rs.getString("accion"),
                        rs.getDate("fecha").toLocalDate(),
                        rs.getTime("hora").toLocalTime().format(DateTimeFormatter.ofPattern("HH:mm:ss")),
                        rs.getString("short")
                )
        );

        return String.join(System.lineSeparator(), filas);
    }
}
